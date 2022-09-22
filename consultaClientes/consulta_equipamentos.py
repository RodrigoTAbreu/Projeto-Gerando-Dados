import sqlite3
banco = sqlite3.connect('olt_banco.db')

cursor = banco.cursor()

#Realiza a pesquisa do banco apresentado todos os dados
cursor.execute("SELECT * FROM equipamentos")

print(cursor.fetchall())