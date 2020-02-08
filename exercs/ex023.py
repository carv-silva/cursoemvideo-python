"""Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

ex: Digite um numero: 1980
unidade:0
dezena:8
centena:9
milhar:1

"""
n = int(input('Digite um numero de 0 a 9999: '))
unid = n % 10
n = (n - unid) / 10
dezena = n % 10
n = (n - dezena) / 10
cent = n % 10
n = (n -cent) / 10
mil = n % 10


dezena = int(dezena)
cent = int(cent)
mil = int(mil)
print(f'Unidade: {unid}\n Dezena: {dezena}\n Centena: {cent}\n Milhar: {mil} ')


'''outro jeito
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
'''




