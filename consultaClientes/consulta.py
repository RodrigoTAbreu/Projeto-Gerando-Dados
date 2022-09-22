#CADASTRA EQUIPAMENTOS NO BANCO DE DADOS

import sqlite3


banco = sqlite3.connect('olt_banco.db')

cursor = banco.cursor()

#Cria a tabela
cursor.execute("CREATE TABLE equipamentos (nome text, gpon text, cidade text)")

#Insere Valores na Tabela

nome = input("NOME DO EQUIPAMENTO: ").upper
gpon = input("GPON: ")
cidade = input("CIDADE: ").upper

cursor.execute("INSERT INTO equipamentos VALUES(f'{nome}', '{gpon}','{cidade}')")

#Salva ou atualiza o banco de dados
banco.commit()


#Realiza a pesquisa do banco apresentado todos os dados
""" cursor.execute("SELECT * FROM equipamentos")

print(cursor.fetchall()) """