from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a jogada? '))
print('-='*20)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-='*20)

if computador == 0: # PREDA
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1: # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 2: # TESOURA
    if jogador ==  0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
