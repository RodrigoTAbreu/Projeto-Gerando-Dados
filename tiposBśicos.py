qtd = int(input('qtd: '))
listaMestra = []
count = 0

n = int(input('Valor de N: '))
listaMestra.insert(0,n)
n = int(input('Valor de N: '))
listaMestra.insert(1, n)
n = int(input('Valor de N: '))
listaMestra.insert(0, n)
print(listaMestra)
n = int(input('Valor de N: '))
listaMestra.remove(n)
n = int(input('Valor de N: '))
listaMestra.append(n)
n = int(input('Valor de N: '))
listaMestra.append(n)
listaMestra.sort()
print(listaMestra)
listaMestra.pop()
listaMestra.reverse()
print(listaMestra)


    count += 1

print(listaMestra)
