'''Refaça o ex009 msotrando a tabuada de um numero que o usuario
escolher, so que agora utilizando um laço for'''


n = int(input('Digite o valor que deseja fazer a tabuada: '))
print('=' * 12)

for i in range(0, 11):
    print(f'{i} x {n:2} = {i*n}')
print('=' * 12)
