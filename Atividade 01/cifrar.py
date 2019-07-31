# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 31/07/2019

import sys
import manip_arquivo as ma
import manip_data as md

# @author Aroldo Felix
# @param data string contendo data no formato DDMMAA
# @param msg mensagem que se deseja criptografar usando a data
# @return mensagem criptografada
def cifrar(data, msg):
	vetor = [[],[]]
	# vetor[0][:] guarda mensagem normal
	# vetor[1][:] guarda mensagem criptografada
	j = 0
	for i in range(len(msg)):
		if(msg[i] != ' ' and msg[i] != '\n'):
			vetor[0].append(msg[i])
			vetor[1].append(chr(ord(msg[i]) + int(data[j])))
			j += 1;
		else:
			vetor[0].append(msg[i])
			vetor[1].append(msg[i])

		if(j >= len(data)):
			j = 0;

	return ''.join(vetor[1])

# @author Aroldo Felix
# @param data string no formato DD/MM/AAAA
# @param msg_file caminho do arquivo que contém o texto a ser criptografado
# @param final_file caminho do arquivo em que se deseja salvar a mensagem criptografada
def main(data, msg_file, final_file):
	data = md.retrieve_data(data)
	
	msg = ma.ler_arquivo(msg_file)

	msg_enc = cifrar(data, msg);

	ma.escrever_arquivo(msg_enc, final_file);


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3])
