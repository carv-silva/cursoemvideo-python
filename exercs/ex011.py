'''Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la
,sabendo que cada litro de tinta, pinta area de 2mquadrado.'''

l = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
a = l * alt
l = a / 2
print(f'A area é {a}m², e a quantidade gasta em litros é: {l}l')
