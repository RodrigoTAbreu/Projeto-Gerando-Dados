import sqlite3
from time import clock_settime, sleep



    #Faz a conexão com o arquivo de banco de dados.
conn = sqlite3.connect('bco_dados.sqlite')
    #chamando o cursor ou em outras palavras abrindo o bco de dados
cur = conn.cursor()

"""execucleatando os comandos no banco de dados"""
#Exclue a tabela candidados se existir
def exclui_tabela():
    cur.execute('DROP TABLE IF EXISTS Candidatos')
    cur.execute('DROP TABLE IF EXISTS Votos')
    
def cria_tabela_candidatos():
    #Cria a tabela Candidados com os campos nome e numero
    cur.execute('CREATE TABLE Candidatos (nome TEXT, numero INTEGER)')

def cria_tabela_votos():
    cur.execute('CREATE TABLE Votos (numero INTEGER)')
    
def cria_tabela_titulo():
    cur.execute('CREATE TABLE Titulo (num_tit INTEGER)')

#Cadastra Candidatos no banco de dados.
def cadastro_candidatos():
    print("Cadastro de Candidatos")
    resp = input("Cadastrar Candidato(a)? [S/N]: ")

    while resp == 's':
        candidato = str(input("Informe o Nome do Candidato(a): "))
        num = int(input("Insira o número do Candidato(a): "))
        cur.execute(f'INSERT INTO Candidatos (nome, numero) VALUES (?,?)', (f'{candidato}', {num}))
        conn.commit()
        resp = input("Continua o cadastro? ")

#Imprime lista de Candidatos cadastrados.
def mostra_candidatos():    
    print('Candidatos: ')
    cur.execute('SELECT nome, numero FROM Candidatos')
    for row in cur:
        print(row)
        
    conn.commit()



def votos():
    print('Digite o número do candidato')
    mostra_candidatos()
    voto = int(input("Digite um dos números acima: "))
    
    cur.execute(f'INSERT INTO Votos (numero) VALUES ({voto})')
    
    
    print('Voto Cadastrado com sucesso.')
    conn.commit()



def resultado():
    print("Resultado")
    cur.execute('SELECT numero FROM Votos')
    for row in cur:
        print(row)


votos()
conn.close()
