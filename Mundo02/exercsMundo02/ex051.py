'''Desenvolva um programa que leia o primeiro termo e a  razao
de uma PA. No final mostre  os 10 primeiros termos dessa progressao'''


print('=' * 23, '\n 10 termo de uma PA')
print('=' * 23)


termo = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = termo + (10-1) * razao

for i in range(termo, decimo + razao, razao):
    print(f'{i}', end=' --> ')
print('Fim') 
