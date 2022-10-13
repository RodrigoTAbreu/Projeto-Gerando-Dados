print("**"*12)
print("\tURNA ELETRONICA")
print("**"*12)

try:
    titulo = int(input("Informe seu Titulo: "))

except ValueError:

    print("Informe apenas valores NUMÉRICOS.")

print("**"*12)
print("\tCANDIDATOS")
print("**"*12)

print("[22] - Bolsonaro")
print("[13] - Lula")
voto = int(input("Digite o Número do seu candidato: "))

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
