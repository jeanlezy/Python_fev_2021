vel = int(input('Insira a velocidade: '))

if vel > 80:
    print('Multado otário, aqui é só a 80 km/h')
    multa = (vel - 80) * 7
    print('Toma ae e paga R${}'.format(multa))
else:
    print('Você ta dentro da lei, puxa o bonde')