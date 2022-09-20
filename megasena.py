
confere= []
repetido = set()

while len(confere) < 6:
    dado = int(input('Digite o numero a ser jogado[0 a 60]: '))
    if dado > 60:
        print('Informe um numero de 0 a 60:')
    else:
        if dado not in confere:
            confere.append(dado)
        else:
            print('Numero informado já foi escolhido, informe outro numero:')
            repetido.add(dado)

confere.sort()
print(f'Números para jogar {confere}. Total de Números {len(confere)}')
print(f'Numeros repetidos {repetido}. Total {len(repetido)}')