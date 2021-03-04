'''Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo '''
import math

a = float(input('Digite um angulo: '))

r = math.radians(a) ## --> tranforma o angulo em radiando para poder fazer a conta

print(f'O angulo de {a} tem o Seno de {(math.sin(r)):.2f}') ## o :.2f --> serve para deixar 2 digito dps da virgula
print(f'O angulo de {a} tem o Cosseno de {math.cos(r):.2f}')
print(f'O angulo de {a} tem o Tangente de {math.tan(r):.2f}')


## segundo metodo
an = float(input('Digite um angulo: '))
print(f'O angulo de: {an} tem o Seno de:{math.sin(math.radians(an)):.2f}')
print(f'O angulo de: {an} tem o Cosseno de:{math.cos(math.radians(an)):.2f}')
print(f'O angulo de: {an} tem o Tangente de:{math.tan(math.radians(an)):.2f}')

