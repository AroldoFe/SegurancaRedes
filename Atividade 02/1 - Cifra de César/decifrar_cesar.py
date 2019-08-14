# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 30/07/2019

# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file):
	arq = open(msg_file, 'r')
	texto = arq.read()
	arq.close()
	return texto

# @author Aroldo Felix
# @param msg conteúdo que se deseja escrever no arquivo
# @param file Caminho do arquivo em que se deseja escrever
def escrever_arquivo(msg, file, chave):
	file = "{}_{}.txt".format(file, chave)
	arq = open(file, 'w')
	arq.write(msg)
	arq.close()

def decifrar(mensagem, alfabeto, chave):
	txt_msg_decifrada = ""
	
	for i in range(len(mensagem)):
		if mensagem[i] not in alfabeto:
			txt_msg_decifrada += mensagem[i]
			continue
		txt_msg_decifrada += alfabeto[(alfabeto.index(mensagem[i]) + chave) % len(alfabeto)]

	return txt_msg_decifrada

def main():
	txt_msg = ler_arquivo("mensagem_oculta.txt")

	alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'
				,'s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J'
				,'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','?',',']

	#print(txt_msg)
	#print(alfabeto[])
	for i in range(len(alfabeto)):
		txt_msg_decifrada = decifrar(txt_msg, alfabeto, i)
		escrever_arquivo(txt_msg_decifrada, "Mensagens Decifradas/cifra_de_cesar", i)

if __name__ == '__main__':
	main()