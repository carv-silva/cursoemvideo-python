'''Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi aludgado.calcule o preco a pagar, sabendoque o carro custa rs$60 por dia e 0.15 por km rodado'''

d = float(input('Qnts dias alugados?'))
k = float(input('Qnts km rodados?'))

print(f'O total a pagar é de R$ {(d*60)+(k*0.15)}')

