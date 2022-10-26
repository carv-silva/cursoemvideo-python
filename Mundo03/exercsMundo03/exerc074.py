'''Crie um programa que vai gerar cinco numeros aleatorios e colocar
em uma tupla. Depois disso mostre a listagem de numeros gerados e
tambem indique a menor e a maior valor que estao na tupla. '''

from random import randint
tupla = tuple(randint(i + 0, 5)for i in range(0, 5))
print(tupla)
print(f'O maior numero sorteado foi: {max(tupla)}')
print(f'O menor numero sorteado foi: {min(tupla)}')




