'''Melhore o jogo do Desafio 028 onde o computador vai pensar em um numero de 0 a 10.
So que agora o jogador vai tentar adivinhar ate acertar mostrando no final quantos palpites foram
necessarios para vencer.'''

'''
from random import randint

escPc = randint(0, 10)

escolha = 0
r = 'S'
count = 0

while r == 'S':
    escolha = int(input('Tente adivinhar um numero de 1 a 10: '))
    count += 1
    if escPc == escolha:
        print(
            f'Voce acertou o numero gerado foi: {escPc} e seu chute:{escolha}')
        print(f'o numero de tentativa foi: {count}')
        exit()
    else:
        print('Voce errou favor tentar novamente...')
        print(f'o numero de tentativa foi: {count}')
        r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')
'''

'''Metodo Guanabara'''

from random import randint

computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um numero de 0 e 10')
print('Sera que vc consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez')

print(f'Acertou com {palpites} tentativas. Parabens')