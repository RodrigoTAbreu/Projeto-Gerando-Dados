from lib2to3.pgen2.token import BACKQUOTE
import sqlite3
import bco_dados
import texto_tela
import os.path


texto_tela.consult_cadidatos()

bco_dados.cadastro_candidatos()
bco_dados.cria_tabela_titulo()
bco_dados.votos()

"""
lista_22 = []
lista_13 = []

if voto == 22:
    lista_22.append(1)
    print(f"Você votou em {voto} Jair M. Bolsonaro. Obrigado por participar.")
elif voto == 13:
    lista_13.append(1)
    print(f"Você votou em {voto} Luis Inácio. Obrigado por participar.")
else:
    print(f"Você digitou {voto}. Seu voto foi nulo!!")

print("**"*22)
print("\tTotal de Votos até o momento.")
print("**"*22)
print(f"Candidato Bolsonaro tem {len(lista_22)} votos.")
print(f"Candidato Lula tem {len(lista_13)} votos.")
"""