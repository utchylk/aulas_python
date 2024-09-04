from time import sleep
from ajuda.lib.interface import *
from ajuda.lib.arquivo import *
arq = 'cursoemvideo.twxt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(('Pessoas cadastradas', 'Cadastrar mais pessoas', 'Sair do sistema'))
    if resposta == 1:
        leiaArquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabeçalho('NOVO REGISTRO!')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Volte sempre!')
        break
    else:
        print('\033[31mErro! Por favor digite uma opção válida!\033[m')
        sleep(1)