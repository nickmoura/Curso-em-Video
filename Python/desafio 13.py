s = float(input('Qual o salário? '))
n = s+(s*15/100)
print('O funcionário que antes recebia um salário de R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(s, n))