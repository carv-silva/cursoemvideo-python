'''Escreva um programa que faca o pc pensar em um numero inteiro entre 0 e 5 e peca
 para o user tentar descobrir qual foi o numero escolhido pelo computador
 obs: o programa devera escrever na tela se o usuario venceu ou perdeu'''

from random import randint

escolha = int(input('Entre com um numero de 0-5: ')) 

nal = randint(0,5)

if nal == escolha :
    print(f'Parabels vc acertou o numero sorteado que é: {nal}')
else:
    print(f'Vc nao acertou burro!! o numero sorteado é: {nal}')