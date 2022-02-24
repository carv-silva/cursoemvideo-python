'''Escreva um programa que leia dois numeros inteiros e compare-os e mostrando
na tela uma seguinte mensagem:
1 - O primeiro valor é Maior
2 - O segundo valor é Maior
3 - Nao existe valor maior, os dois sao iguais'''


primeiroNumero = int(input('Entre com primeiro numero: '))
segundoNumero = int(input('Entre com segundo numero: '))

if primeiroNumero > segundoNumero:
    print(f'O Primeiro numero é maior: {primeiroNumero}')
elif segundoNumero > primeiroNumero:
    print(f'O SEGUNDO numero é maior: {segundoNumero}')
else:
    print('O dois numero sao iguais')

