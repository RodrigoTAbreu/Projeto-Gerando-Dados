#Programa Principal
import consulta_por_bairro
import consulta_por_equipamentos
import consulta_por_condominio
import constul_2


def principal():
    print( "-=" * 20 )
    print( " CONSULTA DE CLIENTES - ROMPIMENTO" )
    print( "-=" * 20 )
    print( '--' * 20 )
    print( '''Escolha a opção de consulta:
        [1] - OLT
        [2] - CTO
        [3] - BAIRRO
        [4] - CONDOMÍNIO
        [5] - SAIR''' )
    escolha = int( input( 'Digite uma das opções: ' ) )

    if escolha == 1:
        consulta_por_equipamentos.equipamento()
    elif escolha == 2:
        constul_2.consultaCTO()
    elif escolha == 3:
        consulta_por_bairro.consulta_bairro()
    elif escolha == 4:
        consulta_por_condominio.consultaCond()
    elif escolha == 5:
        print("Encerrando aplicação.")
    elif escolha > 5:
        print('''Escolha a opção de consulta:
            [1] - OLT
            [2] - CTO
            [3] - BAIRRO
            [4] - CONDOMÍNIO
            [5] - SAIR''')
        escolha = int(input('Digite uma das opções: '))



principal()