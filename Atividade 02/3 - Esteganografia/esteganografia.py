# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 30/07/2019
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file):
	arq = open(msg_file, 'r')
	texto = arq.read()
	arq.close()
	return texto

def esconder_letra_pixel(letra, pixel):
	tupla = []
	for i in range(3):
		tupla.append(pixel[i][:-1] + letra[i])
	return tuple(tupla)

def voltar_inteiro(pixels):
	for ind, pixel in enumerate(pixels):
		r,g,b = pixel
		pixels[ind] = (int(r,2),int(g,2), int(b,2))

	return pixels


def esconder_mensagem(mensagem, pixels_bin):
	indice_imagem = 0
	
	#print(pixels_bin[:6])

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

		pixels_bin[indice_imagem] = pixel1
		pixels_bin[indice_imagem+1] = pixel2
		pixels_bin[indice_imagem+2] = pixel3

		#pixels_criptografado.extend([pixel1,pixel2,pixel3])

		# print(pixel1)
		# print(pixel1_)
		# print()
		# print(pixel2)
		# print(pixel2_)
		# print()
		# print(pixel3)
		# print(pixel3_)
		# print()

		indice_imagem += 3

	# Esconder o [End Of Text]
	
	
	# [End Of Text] invertido
	letra_bin = "110000000"
	
	pixel1 = pixels_bin[indice_imagem]
	pixel2 = pixels_bin[indice_imagem+1]
	pixel3 = pixels_bin[indice_imagem+2]

	pixel1_ = esconder_letra_pixel(letra_bin[:3], pixel1)
	pixel2_ = esconder_letra_pixel(letra_bin[3:6], pixel2)
	pixel3_ = esconder_letra_pixel(letra_bin[6:], pixel3)

	# print(pixel1)
	# print(pixel1_)
	# print()
	# print(pixel2)
	# print(pixel2_)
	# print()
	# print(pixel3)
	# print(pixel3_)
	# print()

	pixels_bin[indice_imagem] = pixel1
	pixels_bin[indice_imagem+1] = pixel2
	pixels_bin[indice_imagem+2] = pixel3
	
	indice_imagem += 3

	return pixels_bin

# @author Aroldo Felix
def main():

	mensagem = ler_arquivo("mensagem.txt")
	#print(mensagem[0:-1])

	img = Image.open("imagem2.bmp").convert("RGB")

	if(img.size[0]*img.size[1] / 3 < len(mensagem)):
		print("Erro: mensagem de tamanho não suportado para a imagem!")
		return
	
	pixels = list(img.getdata())
	#print(pixels[0:5])
	
	# tupla com RGB
	pixels_bin = []
	for pixel in pixels:
		r,g,b = pixel

		pixels_bin.append((bin(r), bin(g), bin(b)))

	#print(bin(ord('a'))[::-1])
	
	# Converter letra em binário e substituir no bit menos significativo da imagem
	pixels_criptografado = esconder_mensagem(mensagem, pixels_bin)
	
	#print(pixels_criptografado[0:6])
	# Voltar pra inteiro

	mensagem_encriptada = voltar_inteiro(pixels_criptografado)

	img_saida = Image.new("RGB", (img.size[0],img.size[1]))
	img_saida.putdata(mensagem_encriptada)
	img_saida.save('final_img.bmp',
    	format = 'BMP',
        quality = 100)
	img_saida.close()


'''
	final_img = Image.fromarray(np.array(pixels_criptografado), 'RGB')
	final_img.save('final_img.bmp')
'''

if __name__ == '__main__':
	main()