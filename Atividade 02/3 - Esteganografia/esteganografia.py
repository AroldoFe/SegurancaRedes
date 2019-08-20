# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 30/07/2019
import sys
from PIL import Image, ImageDraw, ImageFont

# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file):
	arq = open(msg_file, 'r')
	texto = arq.read()
	arq.close()
	return texto

# @author Aroldo Felix
def main():

	mensagem = ler_arquivo("mensagem.txt")

	img = Image.open("imagem2.bmp").convert("RGB")

	if(img.size[0]*img.size[1] / 3 < len(mensagem)):
		print("Erro: mensagem de tamanho não suportado para a imagem!")
		return
	
	pixels = list(img.getdata())
	# tupla com RGB
	pixels_bin = []
	for pixel in pixels:
		r,g,b = pixel

		pixels_bin.append((bin(r), bin(g), bin(b)))

	#print(*pixels_bin[0:0+3])
	print(bin(ord('a'))[::-1])
	# print(bin(127)) # até 127 continua com 7 bits

	r, g, b = pixels_bin[0:3]

	# print(r)
	# print(g)
	# print(b)
	
	# Converter letra em binário e substituir no bit menos significativo da imagem
	indice_imagem = 0
	pixels_criptografado = []

	for caractere in mensagem:

		letra_bin = bin(ord(caractere)).split('b')[1]
		# Deixando no formato 9 bits por letra para melhor tratamento
		while(len(letra_bin) < 9):
			letra_bin = '0' + letra_bin

		letra_bin = letra_bin[::-1]
		# Pegando os pixels em que será salva a letra
		pixel1, pixel2, pixel3 = pixels_bin[indice_imagem, indice_imagem+3]






if __name__ == '__main__':
	main()