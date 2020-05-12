'''Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo
primário e todos as informacoes possiveis sobre ela'''

n = input('Digite algo: ')

print('O tipo desse valor é:{} '.format(type(n)))
print('Só tem espaços ? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É um alfabetico? {}' .format(n.isalpha()))
print('É um alfanumerico? {}'.format(n.isalnum()))
print('Esta em letra maiscula? {}' .format(n.isupper()))
print('Esta em letra maiscula? {}'.format(n.islower()))
print('Esta capitalizada? {}' .format(n.istitle()))

cor = {'pretao_loko': '\033[;1;30;44m'}
