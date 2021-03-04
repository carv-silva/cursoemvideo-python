'''Crie um algoritimo que leia  um numero e mostre o seu dobro triplo e raiz quadrada'''

import math

n = float(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** 0.5
print('O numero é {},\nO dobro é {},\nO triplo é {},\nA raiz quadrada é {:.2f}.' .format(n, d, t, r))

'''Outro metodo'''

n2 = float(input('Digite um numero: '))
r2 = math.sqrt(n2)
print('A raiz quadrada de {} é {}' .format(n2, r2))

