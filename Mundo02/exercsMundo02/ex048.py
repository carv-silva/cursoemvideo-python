'''Faça um programa que calcule a soma entre todos os
numeros impares que sao multiplos de tres e que se
encontram no intervalo de 1 ate 500'''

s = 0
count = 0

for i in range(1, 501, 2):
    if(i % 3 == 0):
        count += 1
        s += i

print(f'A soma dos {count} numeros impares é {s}')

