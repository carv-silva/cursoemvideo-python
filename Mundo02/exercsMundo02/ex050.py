''' Desenvolva um programa que leia seis numeros inteiros e mostre
a soma apenas daqueles que forem pares.Se o valor digitado for impar
desconsidere-lo'''

s = 0
count = 0

for i in range(0, 6):
    n = int(input('Entre com um numero inteiro: '))
    if(n % 2 == 0):
        s += n
        count += 1
print(f'O somatorio dos {count} valores pares, foi: {s}')

