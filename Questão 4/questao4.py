from ftplib import FTP

print('===============================')
print('          [QUESTÃO 4]')
print('===============================')

host = '52.200.142.116'
user = 'ctflteste'
password = 'YdrTXPK#mcG7KUT#H@$P'
fileName = ''
fileContent = ''

ftp = FTP(host)

print('\n~~~~~~~Fazendo login...')
ftp.login(user=user, passwd=password)

files = ftp.nlst()
print('\n~~~~~~~Lista de Arquivos do FTP:', files)

for f in files:
    if f.find('txt') > 0:
        fileName = f

with open('Great Job OK.txt', 'wb') as file:
    ftp.retrbinary(f'RETR {fileName}', file.write)

with open('Great Job OK.txt', 'r') as file:
    fileContent = file.read()
    with open('Questao4.txt', 'w') as fileResult:
        fileResult.write(f'HOST = {host};\nUSUARIO = {user};\nSENHA = {password};\nARQUIVO = {fileName};\nCONTEUDO DO ARQUVIO = {fileContent}')

print('\n~~~~~~~Dados armazenados no arquivo "Questao4.txt"\n')

print('==============FIM==============\n')

ftp.quit()