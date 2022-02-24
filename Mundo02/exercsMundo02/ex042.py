'''Refaça o Desafio 035 dos triangulos acresentando o recurso de mostrar
que o tipo do triangulo é formado:

1 - Equilatero: Todos os lados iguais
2 - Isosceles: Dois lados iguais
3 - Escaleno: Todos os lados diferentes

OBS: para formar o trinagulo tem que a primeira reta tem que ser menor
que a soma do 2 e 3 a segunda reta tem que ser menor que a soma do 3 e do 1
e o 3 reta tem que ser menor que a soma do 1 e 2 '''


a = float(input('Insira o comprimento 1: '))
b = float(input('Insira o comprimento 2: '))
c = float(input('Insira o comprimento 3: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Triangulo Equilatero')
    elif a != b != c != a:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isosceles')
else:
    print('Triangulo nao pode ser formado...')

'''
1 - Equilatero: Todos os lados iguais
2 - Isosceles: Dois lados iguais
3 - Escaleno: Todos os lados diferentes'''




