'''O mesmo professor do desafio anterior quer sortear a ordem de apresentacaoes de trabalhos para alunos.
Faca um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.'''

from random import sample, shuffle
n1 = input('Digite o nome do primeiro aluno: ')

n2 = input('Digite o nome do sgundo aluno: ')

n3 = input('Digite o nome do terceiro aluno: ')

n4 = input('Digite o nome do quarto aluno: ')

list = [n1, n2, n3, n4]

sort = sample(list, 4)
print(sort)

##metodo 2
name1 = input('Digite o nome do primeiro aluno: ')
name2 = input('Digite o nome do sgundo aluno: ')
name3 = input('Digite o nome do terceiro aluno: ')
name4 = input('Digite o nome do quarto aluno: ')

lista  = [name1, name2, name3, name4]
shuffle(lista)
print(lista)
