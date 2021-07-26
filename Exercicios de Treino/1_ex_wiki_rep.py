while True:
    nota = float(input('\nDigite uma nota de 0 a 10:'))
    if nota == 'done':
        break
    elif nota > 10:
        print('Se é burro? {} está entre 0 e 10? Tente novamente.'.format(nota))
    else:
        print('Boa carai, sua nota é {}'.format(nota))
