# @Author Aroldo Felix
# @Data 19/08/2019
# @Update 26/08/2019
import sys
from PIL import Image

# @author Aroldo Felix
# @param letra, 3 binários da letra pra esconder no RGB
# @param pixel, pixel em que se deseja guardar os 3 pixels da letra
# @return pixel RGB modificado com a letra
def esconder_letra_pixel(letra, pixel):
	tupla = []
	for i in range(3):
		tupla.append(pixel[i][:-1] + letra[i])
	return tuple(tupla)

# @author Aroldo Felix
# @param mensagem, mensagem que se deseja esconder na matriz de pixels
# @param pixels_bin, matriz de pixels em binário
# @return matriz de pixels em binário com a mensagem escondida
def esconder_mensagem(mensagem, pixels_bin):
	indice_imagem = 0

	for caractere in mensagem:
		# Removendo o '0b'
		letra_bin = bin(ord(caractere)).split('b')[1]
		# Deixando no formato 9 bits por letra para melhor tratamento
		while(len(letra_bin) < 9):
			letra_bin = '0' + letra_bin

		# Invertendo string de bits para o for i do inicio ao fim da string
		letra_bin = letra_bin[::-1]
		# Pegando os pixels em que será salva a letra
		pixel1 = pixels_bin[indice_imagem]
		pixel2 = pixels_bin[indice_imagem+1]
		pixel3 = pixels_bin[indice_imagem+2]

		# Escondendo a letra em 3 pixeis
		pixel1 = esconder_letra_pixel(letra_bin[:3], pixel1)
		pixel2 = esconder_letra_pixel(letra_bin[3:6], pixel2)
		pixel3 = esconder_letra_pixel(letra_bin[6:], pixel3)

		# Salvando na matriz
		pixels_bin[indice_imagem] = pixel1
		pixels_bin[indice_imagem+1] = pixel2
		pixels_bin[indice_imagem+2] = pixel3

		indice_imagem += 3

	# Esconder o delimitador [End Of Text]
	# [End Of Text] invertido
	letra_bin = "110000000"
	
	pixel1 = pixels_bin[indice_imagem]
	pixel2 = pixels_bin[indice_imagem+1]
	pixel3 = pixels_bin[indice_imagem+2]

	pixel1 = esconder_letra_pixel(letra_bin[:3], pixel1)
	pixel2 = esconder_letra_pixel(letra_bin[3:6], pixel2)
	pixel3 = esconder_letra_pixel(letra_bin[6:], pixel3)

	pixels_bin[indice_imagem] = pixel1
	pixels_bin[indice_imagem+1] = pixel2
	pixels_bin[indice_imagem+2] = pixel3
	
	indice_imagem += 3

	return pixels_bin

# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file):
	arq = open(msg_file, 'r')
	texto = arq.read()
	arq.close()
	return texto

# @author Aroldo Felix
# @param pixels matriz de pixels binários
# @return matriz em inteiro
def voltar_inteiro(pixels):
	for ind, pixel in enumerate(pixels):
		r,g,b = pixel
		pixels[ind] = (int(r,2),int(g,2), int(b,2))

	return pixels

# @author Aroldo Felix
# @param imagem_entrada, caminho da imagem de entrada
# @param imagem_saida, caminho em que será salva a imagem contendo a mensagem escondida
def main(imagem_entrada, imagem_saida):
	# Leitura da mensagem
	mensagem = ler_arquivo('mensagem.txt')
	# Leitura da imagem

	if not(imagem_entrada.endswith('.bmp')):
		imagem_entrada += '.bmp'

	if not(imagem_saida.endswith('.bmp')):
		imagem_saida += '.bmp'

	img = Image.open(imagem_entrada).convert('RGB')

	if(img.size[0]*img.size[1] / 3 < len(mensagem)):
		print('Erro: mensagem de tamanho não suportado para a imagem!')
		return
	# Pegando a matriz de pixels
	pixels = list(img.getdata())
	
	# tupla com RGB
	pixels_bin = []
	for pixel in pixels:
		r,g,b = pixel

		pixels_bin.append((bin(r), bin(g), bin(b)))
	
	# Converter letra em binário e substituir no bit menos significativo da imagem
	pixels_criptografado = esconder_mensagem(mensagem, pixels_bin)
	
	# Voltar pra inteiro

	mensagem_encriptada = voltar_inteiro(pixels_criptografado)

	img_saida = Image.new('RGB', (img.size[0],img.size[1]))
	img_saida.putdata(mensagem_encriptada)
	img_saida.save(imagem_saida,
    	format = 'BMP',
        quality = 100)
	img_saida.close()


if __name__ == '__main__':
	try:
		main(sys.argv[1], sys.argv[2])
	except Exception as e:
		print("Imagem de entrada e/ou de saída não foram inseridas!")
		print()
		print('Esperando algo do tipo: python3 esteganografia.py imagem_entrada.bmp imagem_saida.bmp')