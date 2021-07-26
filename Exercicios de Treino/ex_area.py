altura = float(input('Qual a altura da parede:'))
largura = float(input('Qual a largura da parede:'))
area = altura * largura
tinta = area / 2
print('a sua parede mede {} x {}, tem a area de {}m²'.format(altura, largura, area))
print('Pra pinta essa parede precisara de {}L de tinta'.format(tinta))