from random import choice
n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de mais um aluno: ')
n4 = input('Digite o nome de um quarto aluno: ')
lista = [n1, n2, n3, n4]
print('O aluno sorteado para apagar a lousa é {}.'.format(choice(lista)))
