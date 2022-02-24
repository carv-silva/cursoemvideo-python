'''Exercício 36 – Aprovando Empréstimo
Escreva um programa para aprovar  o emprestimo bancario para a compra de
uma casa.O programa vai perguntar o valor da casa o salario do comprador e
em quantos anos ele vai pagar.
Calcule  o valor da prestação mensal, sabendo que ela nao pode exceder 30%
do  salario ou entao o emprestimo sera negado'''

valorCasa = float(input('Valor da casa: '))
salario = float(input('Salario: '))
anosParcela = int(input('Quantos anos deseja dividir: '))

# totalMeses = (anosParcela * 12)

prestacao = valorCasa / (anosParcela * 12)

porcetagem = (salario / 100) * 30

if prestacao <= porcetagem:
    print(f'Emprestimo aprovado, valor da parcela é {prestacao: .2f}')
else:
    print(f'Negado pois o valor da parcela:{prestacao: .2f}', end='')
    print(' ultrapassa 30% do salario ')
