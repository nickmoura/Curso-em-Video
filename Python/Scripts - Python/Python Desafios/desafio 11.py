l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
ar = l*a
t = ar/2
print('Sua parede tem uma dimensão de {} x {}, tendo uma área de {} m².'.format(l, a, ar))
print('Você precisará de {:.0f} litros de tinta para pintar esta parede.'.format(t))