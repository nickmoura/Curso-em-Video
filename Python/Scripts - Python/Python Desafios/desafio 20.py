from random import shuffle

import emoji

n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('Digite o nome de outro aluno: '))
n3 = str(input('Digite o nome de mais um aluno: '))
n4 = str(input('Digite o nome de um quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Os alunos sorteados são: ')
print(lista)
print(emoji.emojize('Boa sorte! :beaming_face_with_smiling_eyes:'))
