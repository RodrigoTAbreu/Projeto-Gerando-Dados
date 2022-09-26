#CONSULTA DO BANCO DE DADOS POR CTO

def consultaCTO():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    cod_cto = input("Informe a CTO: ").upper()


    print('Resultado: ')
    print('--'*40)

    cursor.execute(f"SELECT olt, pon, cto, nome, condominio, bairro FROM geral WHERE cto = '{cod_cto}'")

    for row in cursor:
        print(row)
    print(cursor.fetchall())



