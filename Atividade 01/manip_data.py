# @Author Aroldo Felix
# @Data 30/07/2019
# @Update 30/07/2019

# @author Aroldo Felix
# @param data string no formato DD/MM/AAAA
# @return string contendo data no formato DDMMAA
def retrieve_data(data):
	data = data.replace('/','')

	init = data[:-4]
	final = data[-2:]

	return init+final