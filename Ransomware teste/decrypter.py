import  os
import pyaes

arquivo_nome = 'documento.txt.ransomware'
arquivo = open(arquivo_nome, 'rb')
dados_arquivo = arquivo.read()
arquivo.close()

chave = b'chavecriptografi'
aes = pyaes.AESModeOfOperationCTR(chave)
dados_decripto = aes.decrypt(dados_arquivo)

os.remove(arquivo_nome)

arquivo_novo = 'documento.txt'
arquivo_novo =  open(f'{arquivo_novo}','wb')
arquivo_novo.write(dados_decripto)
arquivo_novo.close()