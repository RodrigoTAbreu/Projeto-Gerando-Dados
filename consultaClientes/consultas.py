#CONSULTA DO BANCO DE DADOS POR EQUIPAMENTOS E PON

def equipamento():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    olt = input("Informe a OLT: ").upper()
    gpon = input("Informe a GPON: ")

    print('Resultado: ')
    print('--'*40)
    cursor.execute(f"SELECT olt, pon, cto, nome FROM geral WHERE olt = '{olt}' AND pon = 'GPON {gpon}'")
    for row in cursor:
        print(row)
    print(cursor.fetchall())

#CONSULTA DO BANCO DE DADOS POR CTO

def consulta_cto():
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


#CONSULTA DO BANCO DE DADOS POR BAIRRO

def consulta_bairro():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    bairro = input("Informe o bairro: ").upper()


    print('Resultado: ')
    print('--'*40)

    cursor.execute(f"SELECT olt, pon, cto, nome, condominio, bairro FROM geral WHERE bairro = '{bairro}'")

    for row in cursor:
        print(row)
    print(cursor.fetchall())


#CONSULTA DO BANCO DE DADOS POR CONDOMINIO

def consultaCond():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    cond = input("Informe o condomínio: ")

    print('Resultado: ')
    print('--'*40)
    cursor.execute(f"SELECT olt, pon, cto, nome, condominio FROM geral WHERE condominio = '{cond}'")
    for row in cursor:
        print(row)
    print(cursor.fetchall())
