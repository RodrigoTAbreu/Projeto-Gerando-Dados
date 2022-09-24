#Programa Principal
import consulta_cto
import consulta_bairro

def principal():
    print("-="*20)
    print(" CONSULTA DE CLIENTES - ROMPIMENTO")
    print("-="*20)

    print('--'*20)
    print('''Escolha a opção de consulta:
        [1] - OLT
        [2] - CTO
        [3] - BAIRRO
        [4] - CONDOMÍNIO
        [5] - SAIR''')
    escolha = int(input('Digite uma das opções: '))

    while escolha !=5:
        if escolha == 5:
            print("Encerrando aplicação !!")
            break
        if escolha == 2:
            consulta_cto.consult_cto()
        if escolha == 3:
            consulta_bairro.consult_bairro()

principal()


