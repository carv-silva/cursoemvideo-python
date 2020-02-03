'''Faca um algoritimo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto'''

p = float(input('Valor do produto sem desconto: '))

np = (p * 5 / 100 - p) * -1
print('O preco com desconto é: {}'.format(np))
