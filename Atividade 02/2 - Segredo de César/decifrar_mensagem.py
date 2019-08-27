# @author Aroldo Felix
# @param msg_file Caminho do arquivo que se deseja ler
# @return conteúdo do arquivo
def ler_arquivo(msg_file): # OK
	arq = open(msg_file, 'r')
	texto = arq.read()
	arq.close()
	return texto

# @author Aroldo Felix
# @param msg conteúdo que se deseja escrever no arquivo
# @param file Caminho do arquivo em que se deseja escrever
def escrever_arquivo(msg, file, chave):
	file = "Mensagens Decriptadas/{}_{}.txt".format(file, chave)
	arq = open(file, 'w')
	arq.write(msg)
	arq.close()

def get_matriz_alfabeto():
	alfabeto = []

	num_letras = ord('z')-ord('a')+1

	for i in range(0, num_letras):
		lista = []
		for j in range(0, num_letras):
			lista.append((j + i) % num_letras)
		alfabeto.append(lista)

	return alfabeto

def projecao_palavras(mensagem, chave):
	txt_msg = ""

	for i in range(len(mensagem)//len(chave)):
		txt_msg += chave

	txt_msg += chave[:len(mensagem)%len(chave)]

	return txt_msg

def projecao_letra(letra):
	return ord(letra) - ord('a');

def vigenere(msg_encu, msg_proje):
	alfabeto = get_matriz_alfabeto()
	texto_decript = ""

	for i in range(len(msg_encu)):
		# Pego a linha que contem a letra X
		linha = alfabeto[projecao_letra(msg_proje[i])]
		# Pego o índice que contem a letra Y
		pos = linha.index(projecao_letra(msg_encu[i]))
		# Identifico que letra é
		letra = chr(pos + ord('a'))
		# Adiciono ao texto
		texto_decript += letra
	
	return texto_decript

def voltar_msg_original(mensagem, decriptada):
	msg_decript = ""
	ind_dec = 0

	for i in range(len(mensagem)):
		if(mensagem[i] == " "):
			msg_decript += " "
			continue
		else:
			msg_decript += decriptada[ind_dec]
			ind_dec += 1

	return msg_decript

# mensagem é a mensagem normal
# chaves guarda a letra da musica
def decifrar(mensagem, chaves):
	# retiro os espaços pra melhor projeção
	mensagem_encurtada = mensagem.replace(" ", "")
	# separo as senhas
	chaves = list(set(chaves.split(" ")))
	# para cada uma das senhas
	for chave in chaves:
		# projetar cada senha na mensagem sem espaços
		msg_projetada = projecao_palavras(mensagem_encurtada, chave)
		# decriptar a mensagem
		txt_msg = vigenere(mensagem_encurtada, msg_projetada)
		# voltar com os espaços originais
		txt_msg_decriptada = voltar_msg_original(mensagem, txt_msg)
		escrever_arquivo(txt_msg_decriptada, "vigenere", chave)

def remove_caracteres_especiais(texto):
	final_txt = texto.lower()
	final_txt = final_txt.replace("\n\n", " ")
	final_txt = final_txt.replace("\n", " ")
	final_txt = final_txt.replace(",", "")
	final_txt = final_txt.replace("?", "")
	final_txt = final_txt.replace("ç", "c")
	final_txt = final_txt.replace("é", "e")
	
	return final_txt

def main():
	txt_msg = ler_arquivo("mensagem_cifrada.txt")
	#print(txt_msg)
	
	txt_senhas = remove_caracteres_especiais(ler_arquivo("cifra_de_cesar_22.txt"))
	#print(txt_senhas)

	decifrar(txt_msg, txt_senhas)


if __name__ == '__main__':
	main();