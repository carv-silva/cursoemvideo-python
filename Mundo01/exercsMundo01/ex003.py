'''Crie um programa que leia dois numeros e mostre a soma entre eles'''


n1 = float(input('Digite o Primeiro numero: '))
n2 = float(input('Digite o Segundo numero: '))

cor = {'pretao_loko': '\033[;1;30;44m'}

print(f"A soma dos dois numero é:{cor['pretao_loko']} {n1+n2}!")
