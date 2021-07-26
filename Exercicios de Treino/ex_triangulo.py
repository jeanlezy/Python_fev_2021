print('-='*12)
print('Analisador de Triângulos')
print('-='*12)
r1 = int(input('\nLado 1 do triangulo: '))
r2 = int(input('Lado 2 do triangulo: '))
r3 = int(input('Lado 3 do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triângulo carai')
else:
    print('Não é um triângulo, jumento')