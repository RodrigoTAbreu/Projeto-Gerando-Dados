from menu import *
from consultas import *
from time import sleep

while True:
    resposta = menu(['OLT', 'CTO', 'BAIRRO', 'CONDOMÍNIO', 'SAIR'])
    if resposta == 1:
        equipamento()
    elif resposta == 2:
        consulta_cto()
    elif resposta == 3:
        consulta_bairro()
    elif resposta == 4:
        consultaCond()
    elif resposta == 5:
        print('Encerrando Consultas !!!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)

