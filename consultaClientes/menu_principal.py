#Programa Principal
import consultas

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
        consultas.equipamento()
    elif escolha == 2:
        consultas.consulta_cto()
    elif escolha == 3:
        consultas.consulta_bairro()
    elif escolha == 4:
        consultas.consultaCond()
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