'''Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio,pergunte ao usuario qual sera o valor a ser sacado(numero inteiro)
e o programa vai informar quantas celulas de cada valor serao entregues
obs: considere que o caixa possui cedulas de 50, 20, 10 e 1 .'''

print('=' * 30)
print('     BANCO DO CARLAO')
print('=' * 30)

cont = 0
notas = 0
valor = int(input("que valor deseja sacar? R$: "))
total = valor
totalCedula = 0
cedula = 100
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'total de {totalCedula} celulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre no banco do carlão')
