import matplotlib.pyplot as plt


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=2)

#Define o título do gráfico e nomeia os eixos
plt.title('Numeros quadrados', fontsize=18)
plt.xlabel("Valor", fontsize = 12)
plt.ylabel("Valor do Quadrao", fontsize = 12)

#Defineo tamango dos tórulos das marcações.
plt.tick_params(axis='both', labelsize=11)

plt.show()
