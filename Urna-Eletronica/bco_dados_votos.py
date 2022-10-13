import sqlite3

#Faz a conexão com o arquivo de banco de dados.
conn = sqlite3.connect('votos_contabilizados.sqlite') 
#chamando o cursor ou em outras palavras abrindo o bco de dados
cur = conn.cursor()

"""executando os comandos no banco de dados"""
#Exclue a tabela candidados se existir
"""cur.execute('DROP TABLE IS EXISTS Candidatos')"""
#Cria a tabela Candidados com os campos nome e numero
"""cur.execute('CREATE TABLE Candidatos (nome TEXT, numero INTEGER)')"""


print("Cadastro de Candidatos")
resp = input("Cadastrar Candidato(a)? [S/N]: ")


while resp == 's':
    candidato = input("Informe o Nome do Candidato(a): ")
    numero = int(input("Insira o número do Candidato(a): "))
    cur.execute('INSERT INTO Candidatos (nome, numero) VALUES(?,?)', (f'{Padre Kelmom}', 10))
    resp = input("Continua o cadastro? ")



cur.execute('INSERT INTO Candidatos (nome, numero) VALUES (?,?)', ('Simone',23))
conn.commit()

print('Candidatos: ')
cur.execute('SELECT nome, numero FROM Candidatos')
for row in cur:
    print(row)
    
conn.commit()


conn.close()
