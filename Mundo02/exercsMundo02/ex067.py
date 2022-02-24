'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez.
para cada valor digitado pelo usuaro. o programa sera interrompido
quando o numero solicitado for negativo'''

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        print(f'Tabuada encerrada!!!')
        break
    print('=' * 12)
    for i in range(0, 11):
        print(f'{numero} X {i} = {i * numero}')
    print('=' * 12)




