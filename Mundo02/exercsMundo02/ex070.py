'''Crie um programa que leia o nome e o preço de varios produtos . o Programa
devera pergunta se o usuario vai continuar. no final mostre:

A) qual é o total de gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.

'''

print('-' * 30)
print('     LOJAO DO CARLAO')
print('-' * 30)

total = produtos = menor = cont = 0
barato = ''


while True:

    nomeProduto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$: '))
    total += preco
    cont += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nomeProduto

    if preco > 1000:
        produtos += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))


print(f'O total gasto é: R${total}')
print(f'A quantidade de Produtos que custam mais de 1000 é : {produtos}')
print(f'o nome do produto mais barato é : {barato} que custa {menor:.2f}')
