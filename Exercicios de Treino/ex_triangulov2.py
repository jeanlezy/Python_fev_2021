s1 = int(input('1º lado: '))
s2 = int(input('2º lado: '))
s3 = int(input('3º lado: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É um triangulo')
    if s1 == s2 == s3:
        print('EQUILATERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Não é um triangulo')