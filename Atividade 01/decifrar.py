# @Author Aroldo Felix
# @Data 31/07/2019
# @Update 31/07/2019

import sys
import manip_arquivo as ma
import manip_data as md

# @author Aroldo Felix
# @param data string contendo data no formato DDMMAA
# @param msg mensagem que se deseja descriptografar usando data
# @return mensagem descriptografada
def decifrar(data, msg):
	vetor = [[],[]]
	# vetor[0][:] guarda mensagem
	# vetor[1][:] guarda o número que tem que voltar
	j = 0
	for i in range(len(msg)):
		if(msg[i] != ' ' and msg[i] != '\n'):
			vetor[0].append(msg[i])
			vetor[1].append(chr(ord(msg[i]) - int(data[j])))
			j += 1;
		else:
			vetor[0].append(msg[i])
			vetor[1].append(msg[i])

		if(j >= len(data)):
			j = 0;

	return ''.join(vetor[1])

# @author Aroldo Felix
# @param data string no formato DD/MM/AAAA
# @param msg_file caminho do arquivo que contém o texto a ser descriptografado
def main(data, msg_file):
	
	data = md.retrieve_data(data)
	
	msg = ma.ler_arquivo(msg_file)

	msg_enc = decifrar(data, msg);

	print(msg_enc)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
