'''Faca um programa que leia um numero inteiroe mostre na tela o seu sucessor e antecessor'''
n = float(input('Digite um numero: '))

a = n - 1
s = n + 1

print('Numero é: {}, seu antecessor é {} e seu sucessor é {}' .format(n, a, s))


'''Segunda maneira'''

d = float(input('Digite um numero: '))
print('Numero é: {}, seu antecessor é {} e seu sucessor é {}' .format(n, (d-1), (d+1)))
