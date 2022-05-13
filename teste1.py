n = int(input())
aluno_Krishna = [25,26.5,28]
aluno_Arjun = [70, 98, 63]
aluno_Malika = [52, 56, 60]
aluno_Harsh = [ 25, 26.5, 28]
aluno_Anurag = [ 26,28,30]
q_name = input('Nome da Consulta: ')

if q_name == 'Krishna':
    media = sum(aluno_Krishna) / 3
    print(f'{media:.2f}')
elif q_name == 'Harsh':
    media = sum(aluno_Harsh) / 3
    print(f'{media:.2f}')
elif q_name == 'Malika' :
    media = sum(aluno_Malika) / 3
    print(f'{media:.2f}')
elif q_name == 'Anurag':
    media = sum(aluno_Anurag) / 3
    print(f'{media:.2f}')
elif q_name == 'Arjun':
    media = sum(aluno_Arjun) / 3
    print(f'{media:.2f}')



    # n = int(input())
    # aluno_Krishna = [67, 68, 69]
    # aluno_Arjun = [ 70, 98, 63]
    # aluno_Malika = [ 52, 56, 60]
    #
    # if n == 1:
    #     media = (sum(aluno_Krishna)) / 3
    #     print(f'{media:.2f}')
    # elif n == 2 :
    #     media = (sum(aluno_Arjun)) / 3
    #     print(f'{media:.2f}')
    # else:
    #     media = (sum(aluno_Malika)) / 3
    #     print(f'{media:.2f}')
