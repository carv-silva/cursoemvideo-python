'''  Faca um programa que leia um ano qualquer e mostre se ele é bixsexto'''

'''ano = int(input('Entre com uma ano: '))

if (ano % 4) == 0:
    print(f'{ano} é bissexto ')
else:
    print(f'{ano} não é bissexto ')'''

from datetime import date

#metodo pelo guanabara 

ano = int(input('Entre com uma ano: '))

if ano == 0:
    ano = date.today().year

if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissexto ')
else:
    print(f'{ano} não é bissexto ')