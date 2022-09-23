#CONSULTA DO BANCO DE DADOS POR CONDOMINIO

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