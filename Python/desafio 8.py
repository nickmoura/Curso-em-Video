n = float(input('Digite uma distância '))
cm = n*100
mm = n*1000
km = n/1000
hm = n/100
dam = n/10
dm = n*10
print('Esta distância pode ser convertida em: \n {:.4f}km \n {:.4f}hm \n {:.4f}dam \n {:.4f}dm \n {:.4f}cm \n {:.4f}mm'.format(km, hm, dam, dm, cm, mm))