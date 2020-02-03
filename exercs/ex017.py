'''Faca um programa que leia o comprimento do cateto aposto e do cateto adjacente de  um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa'''

from math import sqrt
a = float(input('Entre com o cateto: '))
b = float(input('Entre com o cateto aposto: '))
h = sqrt(a**2+b**2)
print(f'A hipotenusa é: {h:.2f}')


## 2 metodo

from math import hypot
ca = float(input('Entre com o cateto: '))
co = float(input('Entre com o cateto aposto: '))
hip = hypot(ca, co)
print(f'A hipotenusa é: {hip:.2f}')







