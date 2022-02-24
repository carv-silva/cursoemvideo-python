'''Escreva um programa que leia um numero inteiro qualquer e peça para
o usuario escolher qual sera a base de conversao:
1 - Binario
2 - Octal
3 - Hexadecimal'''

numero = int(input('Entre com numero inteiro: '))
# num1 = int(input('Entre com numero inteiro: '))
# num2 = int(input('Entre com numero inteiro: '))


print('''Conversor de Base numerica:

        [1] Converter para Binario
        [2] Converter para Octal
        [3] Converter para Hexadecimal
        [4] Sair do Programa

    ''')


opcao = int(input('Escolha a opção do Menu: '))

if opcao == 1:
    print(f'{numero} convertido para Binario é: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para Octal é: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para Hexadecimal é: {hex(numero)[2:]}')
elif opcao == 4:
    exit()
else:
    print('Digite uma opção valida!!!!')
