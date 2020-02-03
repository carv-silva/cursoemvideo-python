'''Faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento'''

s = float(input('Digite o salario: '))

ns = s * 5 / 100 + s

print('O novo salario com aumento de 15% é: {}'.format(ns))
