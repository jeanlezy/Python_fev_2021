# Nome: maior que 3 caracteres;
nome = input('Digite o nome: ')
while len(nome) <= 3:
    print('Minimo de 3 caracteres. Tente novamente.')
    nome = input('Digite o nome: ')

# Idade: entre 0 e 150;
idade = int(input('Digite a idade: '))
while idade > 150:
    print('Idade entre 0 150. Tente novamente.')
    idade = int(input('Digite a idade: '))

# Salário: maior que zero;
salario = float(input('Difite o salário: '))
while salario < 0:
    print ('Salário tem que ser maior que 0. Tente novamente')
    salario = float(input('Difite o salário: '))

# Sexo: 'f' ou 'm';
sexo = input ('Digite o sexo: ')
while sexo != 'feminino' and sexo != 'masculino':
    print ('Masculino ou Feminino. Tente novamente')
    sexo = input ('Digite o sexo: ')

# Estado Civil: 's', 'c', 'v', 'd';
ec = input('Digite o estado civil: ')
while ec != 'solteiro' and ec != 'casado' and ec != 'viuvo' and ec != 'divorciado':
    print ('Solteiro, Casado, Viuvo ou Divorciado. Tente novamente')
    ec = input('Digite o estado civil: ')

print('\nSeu nome é {} \nTem {} anos \nGanha R${} \nSeu sexo é {} \nSeu estado civil é {}'.format(nome, idade, salario, sexo, ec))