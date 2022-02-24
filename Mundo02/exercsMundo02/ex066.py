'''Crie um programa que leia varios numeros inteiros pelo teclado. O programa
so vai parar quando o usuario digitar o valor 999. que é a condição de parada.
No final mostre quantos numeros foram digitados e qual foi a soma entre
eles (descosiderando o flag)'''

soma = cont = 0
while True:
    numero = int(input('Digite um numero (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A Quantidade de numeros é: {cont} e a soma é: {soma}')

