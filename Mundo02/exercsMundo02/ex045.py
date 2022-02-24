'''Crie um programa que faça o computador jogar Jakenpo com vc
Pedra
papel
tesoura '''
from random import randint
from time import sleep

print(''' *--* Bem vindo ao jogo do jankenpo, escolha sua opcao:

            [0] Pedra
            [1] Papel
            [2] Tesoura
            [3] Sair do Programa
    ''')
itens = ('Pedra', 'Papel', 'Tesoura')
escolha = int(input('Escola sua jogada: '))
print('JA')
sleep(2)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=' * 11)
maquina = randint(0, 2)

if escolha == maquina:
    print(f'Vcs empataram, Maquina: {(itens[maquina])}')
    print(f'Sua escolha: {(itens[escolha])}')
elif escolha == 0 and maquina == 1:
    print(f'Vc perdeu, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu {(itens[escolha])}...')
elif escolha == 0 and maquina == 2:
    print(f'Vc ganhou, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu: {(itens[escolha])}...')
elif escolha == 1 and maquina == 0:
    print(f'Vc ganhou, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu: {(itens[escolha])}...')
elif escolha == 1 and maquina == 2:
    print(f'Vc perdeu, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu: {(itens[escolha])}...')
elif escolha == 2 and maquina == 0:
    print(f'Vc perdeu, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu: {(itens[escolha])}...')
elif escolha == 2 and maquina == 1:
    print(f'Vc ganhou, Maquina escolheu: {(itens[maquina])}')
    print(f'Vc escolheu: {(itens[escolha])}...')
elif escolha == 3:
    exit(2)
else:
    print('Faça uma escolha valida!!!')

print('-=' * 11)
