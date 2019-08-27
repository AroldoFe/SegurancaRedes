import sys
from PIL import Image

# @author Aroldo Felix
# @param char_bin, caractere em binario
# @return caractere interpretado
def converter_letra(char_bin):
	return chr(int(char_bin, 2))

# @author Aroldo Felix
# @param pixels, 3 pixels que tem o caractere escondido
# @return caractere escondido revelado
def revelar_caractere(pixels):
	letra = ""
	for pixel in pixels:
		for n in pixel:
			letra = n[-1] + letra

	return letra[1:]

# @author Aroldo Felix
# @param pixels_bin, matriz de pixels da imagem em binário
# @return mensagem que estava escondida nos pixels
def revelar_mensagem(pixels_bin):
	indice = 0
	mensagem = ""

	for indice in range(0, len(pixels_bin)//3, 3):
		# Uma letra é escondida em 3 pixels
		pixel1 = pixels_bin[indice]
		pixel2 = pixels_bin[indice+1]
		pixel3 = pixels_bin[indice+2]
		
		caractere_bin = revelar_caractere([pixel1, pixel2, pixel3])
		# Caractere delimitador [End Of Text]
		if(caractere_bin == '00000011'):
			break

		caractere = converter_letra(caractere_bin)

		mensagem = mensagem + caractere

	return mensagem

# @author Aroldo Felix
# @param caminho_imagem, caminho da imagem que contém a mensagem escondida
def main(caminho_imagem):

	if not(caminho_imagem.endswith('.bmp')):
		caminho_imagem += '.bmp'
	
	img = Image.open(caminho_imagem).convert('RGB')

	pixels = list(img.getdata())

	pixels_bin = []
	for pixel in pixels:
		r,g,b = pixel

		pixels_bin.append((bin(r), bin(g), bin(b)))


	mensagem = revelar_mensagem(pixels_bin)

	print(mensagem)

if __name__ == '__main__':
	try:
		main(sys.argv[1])	
	except Exception as e:
		print("Imagem de entrada não foi inserida ou foi inserida de maneira errada!")
		print()
		print("Esperando algo do tipo: python3 decriptar.py imagem.bmp")
	