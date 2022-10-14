import matplotlib.pyplot as plt

'''
Definindo valores de X e Y manualmente
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
'''
#Calculando dados automaticamente
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,c =y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)

#Define o título do gráfico e nomeia os eixos X e Y
plt.title("Numeros Quadrados", fontsize=22)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado de Valor", fontsize=14)

#Define o intervalo para cada eixo
plt.axis([0,1100,0,1100000])

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both',which='major', labelsize=14)

#Gera um arquivo com o gráfico gerado
plt.savefig('squares_plot.png', bbox_inches='tight') 

#Exibe o gráfico gerado na tela
plt.show()