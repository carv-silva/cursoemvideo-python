''' Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao
formar um trinagulo '''

'''a = float(input('Insira o comprimento 1: '))
b = float(input('Insira o comprimento 2: '))
c = float(input('Insira o comprimento 3: '))

if a + b + c == 180:
    print('Tringulo formado')
else:
    print('Tringulo nao formado')'''
'''para formar o trinagulo tem que a primeira reta tem que ser menor que a soma do 2 e 3 
a segunda reta tem que ser menor que a soma do 3 e do 1 
e o 3 reta tem que ser menor que a soma do 1 e 2'''


#metodo do guanabara ---> o meu esta errado 

a = float(input('Insira o comprimento 1: '))
b = float(input('Insira o comprimento 2: '))
c = float(input('Insira o comprimento 3: '))


if a < b + c and b < a + c and c < a + b:
    print('Tringulo pode ser formado')
else:
    print('Tringulo nao pode ser formado')    



