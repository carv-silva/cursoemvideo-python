'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero ate vinte.
Seu programa devera ler um numero pelo teclado(entre 0 e 20) e monstra-lo
por extenso. '''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

pos = -1
while pos < 0 or pos > 20:
    
    pos = int(input('Digite um número entre 0 e 20: '))
    if  pos > 20:
        print('Tente novamente...!!!') 
print(f'Você digitou o número {numeros[pos]}')


    
    


