from datetime import date
'''A confederação Nacional de natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
1 - Ate 9 anos: Mirim
2 - Ate 14 anos: Infantil
3 - Ate 19 anos: Junior
4 - Ate 20 anos: Senior
5 - Acima: Master'''

dataAtual = date.today().year

anoNasc = int(input('Entre com a data de nascimento: '))

if anoNasc > dataAtual:
    print('O ano de nascimento nao pode ser maior que o atual')

idade = dataAtual - anoNasc

if idade <= 9:
    print(f'Sua idade é: {idade}, portanto vc é Natador Mirim')
elif idade <= 14:
    print(f'Sua idade é: {idade}, portanto vc é Natador Infantil')
elif idade <= 19:
    print(f'Sua idade é: {idade}, portanto vc é Natador Junior')
elif idade <= 20:
    print(f'Sua idade é: {idade}, portanto vc é Natador Senior')
else:
    print(f'Sua idade é: {idade}, portanto vc é Natador Master')

