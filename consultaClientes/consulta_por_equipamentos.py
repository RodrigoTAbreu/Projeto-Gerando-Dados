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