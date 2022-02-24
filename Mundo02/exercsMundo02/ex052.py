'''Faça um programa que leia um numero inteiro e diga se ele é
ou nao um numero primo
OBS: Numero primero é divisao por 1 e por ele mesmo '''


num = int(input('Digite um numero inteiro: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')
print(f'\n\033[m O numero {num} foi divisivel {total} vezes. ')

if total == 2:
    print('E por isso ele é primo ')
else:
    print('E por isso ele nao é primo ')
