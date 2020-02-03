import math
'''from math import sqrt --> importa apenas o modulo sqrt '''
num = float(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {} '.format(num, math.ceil(raiz)))

#parte 2  imortando n/ aleatorios

import random

num = random.randint(1, 10)
print(num)

# importando bibliotecas do site Exemplo: biblioteca de emoji

import emoji

print(emoji.emojize("Hello :zap:", use_aliases=True))





