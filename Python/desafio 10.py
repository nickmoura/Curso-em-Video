n = float(input('Quantos reais você tem na carteira? R$ '))
d = n/5.14
e = n/5.08
print('Com R$ {:.2f}, você pode comprar $ {:.2f} e € {:.2f}.'.format(n, d, e))