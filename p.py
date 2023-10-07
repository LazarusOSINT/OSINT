#Autor LazarusOSINT 
#profsilvio@aol.com
import os

diretorio = '/caminho/do/seu/diretorio'  # Substitua pelo caminho do seu diretório

# Itera sobre os arquivos no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.doc'):
        print(f'Arquivo .doc encontrado: {arquivo}')
