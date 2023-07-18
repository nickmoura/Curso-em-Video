dias = int(input('Por quantos dias você alugou o carro? '))
kms = float(input('Quantos km você percorreu com o carro? '))
pago = (dias * 60) + (kms * 0.15)
print('Você pagará R$ {:.2f} pelo aluguel do carro.'.format(pago))