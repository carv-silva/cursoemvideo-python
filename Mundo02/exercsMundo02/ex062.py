'''Melhore o desafio 61 perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disse que quer mostrar 0 termos.'''

'''
print('=' * 23, '\n 10 termo de uma PA')
print('=' * 23)


termo = int(input('Primeiro Termo: '))  # 10
razao = int(input('Razao: '))  # 5
cont = 1

# decimo = termo + (10-1) * razao # 55

while cont <= 10:
    if cont < 10:
        print(f'{termo}', end=' --> ')
    elif cont == 10:
        print(f'{termo}', end=' --> ')
    termo += razao
    cont += 1
r = str(input('\nQuer continuar? [S/N]: ')).upper()
if r == 'S':
    n = int(input("Quantos elementos deseja  exibir a mais?: "))
    if n >= 0:
        ultimo = termo + (n-1) * razao
        ultimo = ultimo + 1
        for i in range(termo, ultimo, razao):
            print(f'{i}', end=' --> ')
        print('Fim')
    else:
        exit()
else:
    exit()

   while cont <= termoAdiconal:
        if cont < termoAdiconal:
            print(f'{termo}', end=' --> ')
        elif cont == termoAdiconal:
            print(f'{termo}', end=' --> ')
        termo += razao
        cont += 1
'''


# Correcao do guanabara

print('=' * 23, '\n Gerador de uma PA')
print('=' * 23)

termo = int(input('Primeiro Termo: '))  # 10
razao = int(input('Razao: '))  # 5
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} --> ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termo voce quer a mais?: '))
print(f'Progressao finalizada, total de termos:{total}')

