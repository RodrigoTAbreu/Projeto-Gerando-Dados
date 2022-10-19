from menu import *
from consultas import *
from time import sleep



while True:
    resposta = menu(['OLT', 'CTO', 'BAIRRO', 'CONDOMÍNIO', 'CLIENTE', 'SAIR'])
    if resposta == 1:
        print(linha())
        equipamento()
        sleep(1)
    elif resposta == 2:
        print(linha())
        consulta_cto()
        sleep(1)
    elif resposta == 3:
        print(linha())
        consulta_bairro()
        sleep(1)
    elif resposta == 4:
        print(linha())
        consultaCond()
        sleep(1)
    elif resposta == 5:
        print(linha())
        consulta_cliente()
        sleep(1)
    elif resposta == 6:
        print('Encerrando Consultas !!!')
        print(linha())
        sleep(2)
        break
    else:
        print('[ERRO]! Digite uma opção válida!')
        sleep(2)

