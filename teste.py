# notas = {'João': 9,
#          'Maria': 10,
#          'Amanda': 9.5,}
#
# nome = input("Digite o nome do aluno: ")
#
#
# if notas.get(nome):
#     print(f"Já existe esse aluno cadastrado. {nome}")
#     print(f"A nota cadastrada para esse aluno é {notas[nome]}")
# else:
#     nota = float(input("Nota do aluno: "))
#     notas[nome] = nota
# print(notas)

qtd = int(input('Quantidade de Registros: '))

alunos = {}
aluno1 = {}
aluno2 = {}
aluno3 = {}
media1 = media2 =  media3 = int


for n in range(0,qtd):
    if n == 0 :
        aluno1[0] = input('Nome: ')
        aluno1[1] = int(input('Nota1: '))
        aluno1[2] = int(input('Nota2: '))
        aluno1[3] = int(input('Nota3: '))
        media3 = (aluno1[1] + aluno1[2] + aluno1[3]) / 3
        print(media1)

    if n == 1 :
        aluno2[0] = input('Nome: ')
        aluno2[1] = int(input('Nota1: '))
        aluno2[2] = int(input('Nota2: '))
        aluno2[3] = int(input('Nota3: '))
        media3 = (aluno2[1] + aluno2[2] + aluno2[3]) / 3
        print(media2)

    if n == 2:
        aluno3[0] = input('Nome: ')
        aluno3[1] = int(input('Nota1: '))
        aluno3[2] = int(input('Nota2: '))
        aluno3[3] = int(input('Nota3: '))
        media3 = (aluno3[1] + aluno3[2] + aluno3[3]) / 3
        print(media3)

    # alunos[0] = aluno1
    # alunos[1] = aluno2
    # alunos[2] = aluno3


print(alunos)
print("Fim")

# aluno = {}
# aluno1 = ['Aline',5,7,9]
# aluno2 = ['Carla',7,9,5]
# aluno3 = ['Maria',8,5,7]
# aluno[0]=  aluno1
# aluno[1] = aluno2
# aluno[2] = aluno3
# print(aluno)