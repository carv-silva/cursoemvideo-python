'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')


n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('Fim')
'''
r = 'S'

while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')
'''
par = impar = 0

n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} impares')'''
