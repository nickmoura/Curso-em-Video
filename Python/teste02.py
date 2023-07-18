p = float(input('Quanto custa o produto? '))
d = p-(p*10/100)
a = p+(p*8/100)
print('O valor do produto é R$ {}. Com 10% de desconto, à vista sairá por R$ {} e, com ágio de 8%, R$ {} parcelado.'.format(p, d, a))