'''Escreva um pograma que pergunte o salario do funcionario e calcule o valor do seu aumento
para salario superior a R$1250 calcule um aumento de 10%
para salario inferior um aumento de 15%'''  

sal = float(input('Insira seu salario: '))

if sal <= 1250 :
    novoSal = (sal / 100 * 15) + sal
else:
    novoSal = (sal / 100 * 10) + sal

print(f'Seu salario normal {sal:.2f} com aumento é: R${novoSal:.2f}')