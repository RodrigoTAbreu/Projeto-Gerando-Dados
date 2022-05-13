import random
import matplotlib.pyplot as plt
from time import sleep


print("-="*20)
print("Gerador de Números - MEGA SENA")
print("-="*20)

count = 0
jogo = []
print("Gerando Números.")
sleep(1)
print("..")
sleep(1)
print("..")
sleep(1)

while count < 6:
    n = random.randint(1,60)
    jogo.append(n)
    busca = jogo.index(n)

    if busca in jogo :
        jogo.remove(busca)
    count += 1

print(f"Seu jogo é de {len(jogo)} números.")
print(f"Os números da sorte são: {sorted(jogo)}. Boa sorte !!")
print("-="*20)
print("Veja um Gráfico com os números !!")

#Gráfico dos números Gerados
plt.plot(jogo, linewidth=3)

plt.title("Números Gerados", fontsize=20)
plt.xlabel("Valores(x)", fontsize = 14)
plt.ylabel("Valores(y)", fontsize = 14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

plt.show()