'''Crie um programa que leia varios numeros inteiros pelo teclado.
o programa so vai parar quando o usuario digitar 999, que é a condição
de parada. No final mostre quantos numeros foram digitados e qual foi
a soma entre eles (desconsiderando o flag)'''
'''
n = 0
list = []


while n != 999:

    n = int(input('Digite um numero inteiro: '))
    #n.append(int(input('Digite um numero: ')))
    #del n[-1]
    #s = sum(n)
    list.append(n)
    #s += n

#list = list.append(n)
del list[-1]
#print(list)
soma = sum(list)
print(f'A soma é: {soma}')'''

# metodo guanabara

n = cont = soma = 0
n = int(input('Digite um numero: '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero: '))
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')





