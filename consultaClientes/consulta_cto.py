#CONSULTA DO BANCO DE DADOS POR CTO
import menu_principal

def consult_cto():
    import sqlite3 #importa a lib do sql
    banco = sqlite3.connect('olt_banco.db') #variavel se conecta ao bando de dados

    cursor = banco.cursor()

    #Realiza a pesquisa do banco apresentado todos os dados

    cto = input("Informe a CTO: ").upper()

    print('Resultado: ')
    print('--'*40)
    #Realiza a consulta com base na tabela GERAL apresentadno os dados somente desta tabela.
    #cursor.execute(f"SELECT olt, pon, cto, nome, condominio FROM geral WHERE cto = '{cto}'")
    #for row in cursor:
    #    print(row)

    #Realiza a pesquisa vinculando a consulta com duas tabelas distintas, com base na CTO que é campo em comum nas duas tabelas
    cursor.execute(f"SELECT olt, pon, dados_cliente.CODCLIENTE, dados_cliente.CLIENTE FROM geral INNER JOIN dados_cliente on geral.cto = dados_cliente.cto WHERE geral.cto = '{cto}'")
    for row in cursor:
        print(row)

    print(cursor.fetchall())

    menu_principal.principal()