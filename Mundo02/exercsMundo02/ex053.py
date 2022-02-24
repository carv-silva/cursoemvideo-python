''' Crie um programa que leia uma frase qualquer e diga se ela
é palindromo, desconsiderando os espaço
OBS: palindromo é a frase que vc le de tras pra frente e é a mesma coisa
EX:
Apos a sopa
a sacada da casa
a torre da derrota'''


frase = str(input('Entre com a frase: '))

print(f'A frase que vc digitou é: {frase}')

frase = frase.replace(" ", "").lower()

palindromo = frase[::-1]

print(f'O inverso de {frase} é {palindromo}')

if frase == palindromo:
    print('A frase é palindromo')
else:
    print('A frase nao é palindromo')


'''print(len(frase))
frase.lower()
#
# s.replace(" ", "")
# frase.strip(" ")
# frase[::-1]
# print(palindromo)

# txt.strip(",.grt")

# print(frase[::-1])

invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print(f'A frase que você digitou invertida fica: {invertida}')'''
