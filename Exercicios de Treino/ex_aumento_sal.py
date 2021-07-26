sal = float(input('Qual o salário: '))
if sal > 1250:
    mod = sal + (sal * 0.1)
else:
    mod = sal + (sal * 0.15)
print('O salário de R${} teve um aumento para R${}'.format(sal, mod))