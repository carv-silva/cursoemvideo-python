'''Refaça o desafio 051 lendo o primeiro termo de uma razao de uma pa
mostrando os 10 primeiros termos da progreessao usando a estrutura
while.'''

print('=' * 23, '\n 10 termo de uma PA')
print('=' * 23)


termo = int(input('Primeiro Termo: ')) # 10
razao = int(input('Razao: ')) # 5
cont = 1
# decimo = termo + (10-1) * razao # 55

while cont <= 10:
    if cont < 10:
        print(f'{termo}', end=' --> ')
    elif cont == 10:
        print(f'{termo}', end=' --> ')
    termo += razao
    cont += 1
print('Fim')

'''Metodo guanabara'''


while cont <= 10:
    print(f'{termo} -->', end='')
    termo += razao
    cont += 1
print('Fim')
