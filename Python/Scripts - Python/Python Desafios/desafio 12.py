p = float(input('Preço em R$ '))
n = p-(p*5/100)
print('O produto que custava R$ {:.2f}, na promoção custará R$ {:.2f}.'.format(p, n))
