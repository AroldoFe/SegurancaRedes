# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 30/07/2019

# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file):
	arq = open(msg_file, 'rb')
	img = arq.read()
	arq.close()
	return img

# @author Aroldo Felix
# @param msg conteúdo que se deseja escrever no arquivo
# @param file Caminho do arquivo em que se deseja escrever
def escrever_arquivo(msg, file):
	arq = open(file, 'w')
	arq.write(msg)
	arq.close()


def main():
	img = ler_arquivo('tiger.bmp')
	print(img)

if __name__ == '__main__':
	main()