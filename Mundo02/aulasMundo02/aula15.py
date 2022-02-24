'''cont = 1
while cont <= 10:
    print(cont, '--> ', end='')
    cont += 1
print('Acabou')


# while True: --> laço infinito
n = cont01 = 0

while cont01 != 3:
    n = int(input('Digte um numero: '))
    cont01 += 1'''

# fleg --> significa que acabou

# no python vc nao declara variavel vc inicializa

n = s = 0
while True:
    n = int(input('Digte um numero: '))
    if n == 999:
        break
    s += n
print(f'a soma dos numeros foi {s}')
print('Acabou')
