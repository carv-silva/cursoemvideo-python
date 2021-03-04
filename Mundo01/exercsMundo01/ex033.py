'''Faca um programa que leia tres numero e mostre qual é maior e qual é menor.'''

n = float(input('Entre com um numero aleatorio: '))
f = float(input('Entre com um numero aleatorio: '))
g = float(input('Entre com um numero aleatorio: '))

maior = n

if(f > n):
    maior = f
if(g > maior):
    maior = g
print(f'Maior numero é {maior}')

#### menor

menor = n

if(f < n):
    menor = f
if(g < maior):
    menor = g
print(f'Menor numero é {menor}')

# metodo do guanabara 


 

