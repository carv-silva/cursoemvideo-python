from datetime import date
'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda nao atingiram maioridade e qnts
ja sao maiores
OBS:Considedar 21  como ano de maioridade'''
dataAtual = date.today().year
s = 0
count = 0
countMenor = 0

for i in range(1, 8):

    anoNasc = int(input('Entre com seu ano de nascimento: '))
    idade = dataAtual - anoNasc

    if anoNasc > dataAtual:
        print('O ano de nascimento nao pode ser maior que o atual')

    if idade >= 21:
        count += 1
    else:
        countMenor += 1

print(f'{count} Sao maiores de 21')
print(f'{countMenor} Sao menores de 21 ')


