import matplotlib.pyplot as plt

'''
Definindo valores de X e Y manualmente
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
'''
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, s=20)

#Define o título do gráfico e nomeia os eixos
plt.title("Numeros Quadrados", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado de Valor", fontsize=14)

#Define o intervalo para cada eixo
plt.axis([0,1100,0,1100000])

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both',which='major', labelsize=14)


plt.show()