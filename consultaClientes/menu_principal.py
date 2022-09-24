#Programa Principal
import consulta_por_cto
import consulta_por_bairro
import consulta_por_equipamentos

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

    while escolha <= 5:
        if escolha == 5:
            print("Encerrando aplicação !!")
            break
        if escolha == 2:
            consulta_por_cto.consulta_cto()
        if escolha == 3:
            consulta_por_bairro.consulta_bairro()
        if escolha == 1:
            consulta_por_equipamentos.equipamento()
        if escolha > 5:
            print('''Escolha a opção de consulta:
                    [1] - OLT
                    [2] - CTO
                    [3] - BAIRRO
                    [4] - CONDOMÍNIO
                    [5] - SAIR''')
            escolha = int(input('Digite uma das opções: '))
principal()


