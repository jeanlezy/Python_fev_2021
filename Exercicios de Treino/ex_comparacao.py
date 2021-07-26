n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O primeiro valor é maior que o segundo.')
else:
    print('O segundo valor é maior que o primeiro.')