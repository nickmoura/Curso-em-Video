import math
lo = float(input('Digite o comprimento do lado oposto: '))
la = float(input('Digite o comprimento do lado adjacente: '))
h = math.hypot(lo, la)
print('A hipotenusa vai ser {:.2f} cm.'.format(h))