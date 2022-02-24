from math import factorial

'''Faca um programa que leia um numero qualquer e o mostre o seu fatorial
EX: 5! 5X4X3X2X1 = 120'''

'''
n = int(input('Digite um numero inteiro qualquer: '))
fat = 1
i = 1

while i <= n:
    fat *= i
    i += 1
print(fat)

resultado = 1
numero = int(input('Digite um numero inteiro qualquer: '))

for n in range(1, numero + 1):
    resultado *= n

print(resultado)'''


'''Metodo guanabara'''


'''n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')
'''

'''Outro metodo'''

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
soma = 1
print(f'calculando {n}! =')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    soma *= c
    c -=1
print(f'{soma}')


