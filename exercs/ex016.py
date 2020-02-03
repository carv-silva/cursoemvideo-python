'''Crie um programa que leia um numero Real qualquer pelo teclado e mostre  na tela sua porcao inteira '''
'''Ex:Digite um numero: 6.127
o numero 6.127 tem a parte inteira  6'''
from math import trunc
n = float(input("Digite um numero: "))

print(f'O numero:{n} tem a parte inteira {trunc(n)}')

##metodo 2
n2 = float(input('Digite um numero: '))
print(f'O numero: {n} tem a parte inteira: {int(n)}')


