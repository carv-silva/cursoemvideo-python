'''Crie um programa que leia dois valores e motre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa,
seu programa devera realizar a operacao solicitada em cada caso '''

'''
# s = 0
r = 'S'
lista = []


while r == 'S':
    valor_one = float(input('Entre com 1 valor: '))
    valor_two = float(input('Entre com 2 valor: '))
    lista = [valor_one, valor_two]

    print(Calculadora:

        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa

    )

    opcao = int(input('Escolha a opção do Menu: '))

    if opcao == 1:
        print(
            f'A soma do {valor_one} e do {valor_two} é {valor_one + valor_two }')
        exit()
    elif opcao == 2:
        print(
            f'A multipliacao do {valor_one} e do {valor_two} é {valor_one * valor_two }')
        exit()
    elif opcao == 3:
        print(f'O maior numero digitado é { max(lista)}')
        exit()
    elif opcao == 4:
        r = 'S'
    elif opcao == 5:
        exit()
    else:
        print('Digite uma opção valida!!!!')

print('Fim')
'''

'''Metodo Guanabara'''

from time import sleep

n1 = int(input('Entre com 1 valor: '))
n2 = int(input('Entre com 2 valor: '))
opcao = 0

while opcao != 5:
    print('''Calculadora:

        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa

    ''')
    opcao = int(input('Escolha a opção do Menu: '))
    if opcao == 1:
        print(
            f'A soma do {n1} + {n2} é {n1 + n2 }')
    elif opcao == 2:
        print(
            f'A multipliacao do {n1} * {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Entre com 1 valor: '))
        n2 = int(input('Entre com 2 valor: '))
    elif opcao == 5:
        print('Finalizado...')
        sleep(2)
        exit()
    else:
        print('Opcao invalida.. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa')
