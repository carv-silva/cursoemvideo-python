'''Um professor quer sortear um dos  seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles
e escrevendo o nome do escolhido'''

from random import sample, choice
n1 = input('Digite o nome do primeiro aluno: ')

n2 = input('Digite o nome do sgundo aluno: ')

n3 = input('Digite o nome do terceiro aluno: ')

n4 = input('Digite o nome do quarto aluno: ')

list = [n1, n2, n3, n4]

sort = sample(list, 1)
print(sort)

## metodo 2
name1 = input('Digite o nome do Primeiro aluno: ')
name2 = input('Digite o nome do Sgundo aluno: ')
name3 = input('Digite o nome do Terceiro aluno: ')
name4 = input('Digite o nome do Quarto aluno: ')
lista = [name1, name2, name3, name4]
escolha = choice(lista)
print(f'O escolhido é {escolha}')


