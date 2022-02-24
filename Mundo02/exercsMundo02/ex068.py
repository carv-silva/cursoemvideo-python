'''Faca um programa que jogue par ou impar com o computador. o jogo so sera
interrompido quando o jogador perder. mostranddo o total de vitorias
consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep
soma = cont = 0


while True:
    print('=-' * 17)
    print(' VAMOS JOGAR UM JOGO PAR OU IMPAR ')
    print('=-' * 17)

    numero_jogador = int(input('Digte um valor: '))
    escolha_jogador = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    print('=-' * 17)
    maquina = randint(0, 11)
    soma = numero_jogador + maquina

    if escolha_jogador == 'P':
        if soma % 2 == 0:
            print(f'Voce jogou {numero_jogador} e o computador jogou {maquina}. o Total deu {soma} PAR')
            print('Voce VENCEU!!!! \n Vamos jogar novamente .....')
            print('=-' * 17)
            cont += 1
        else:
            print(
                f'Voce jogou {numero_jogador} e o computador jogou {maquina}. o Total deu {soma} IMPAR')
            print('Voce Perdeu!!!!')
            print('=-' * 17)
            print(f'GAME OVER! Voce venceu {cont} vezes.')
            break
    if escolha_jogador == 'I':
        if soma % 2 != 0:
            print(
                f'Voce jogou {numero_jogador} e o computador jogou {maquina}. o Total deu {soma} IMPAR')
            print('Voce VENCEU!!!! \n Vamos jogar novamente .....')
            print('=-' * 17)
            cont += 1
        else:
            print(
                f'Voce jogou {numero_jogador} e o computador jogou {maquina}. o Total deu {soma} PAR')
            print('Voce Perdeu!!!!')
            print('=-' * 17)
            print(f'GAME OVER! Voce venceu {cont} vezes.')
            break'''

# metodo guanabara


from random import randint
v = 0

while True:
    jogador = int(input('Digte um valor: '))
    maquina = randint(0, 11)
    total = jogador + maquina
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print(
        f'Voce jogou {jogador} e o computador jogou {maquina}. Total de {total} ', end='')
    print(f' DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 != 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 1:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Voce venceu {v} vezes.')




