dist = (float(input('Qual a distância da viagem: ')))
if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = dist * 0.45
print('Sua passagem vai custar:', passagem)
