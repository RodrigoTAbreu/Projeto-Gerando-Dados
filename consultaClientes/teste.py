def contador(i,f,p):
    """
    :param i: Valor de Inicio
    :param f:  Valor de Fim
    :param p: Valor de passo
    :return: Retorna o contador com inicio(i), Fim(f) e Passo(p)
    Função criada por Rodrigo
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


#contador(2,10,2)
help(contador)
