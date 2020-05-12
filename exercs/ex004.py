'''Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo
primário e todos as informacoes possiveis sobre ela'''

n = input('Digite algo: ')

print(f'O tipo desse valor é: {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É um alfabético? {n.isalpha()}')
print(f'É um alfanumérico? {n.isalnum()}')
print(f'Esta em letra maiúscula? {n.isupper()}')
print(f'Esta em letra minúscula? {n.islower()}')
print(f'Esta capitalizada? {n.istitle()}')

cor = {'pretao_loko': '\033[;1;30;44m'}
