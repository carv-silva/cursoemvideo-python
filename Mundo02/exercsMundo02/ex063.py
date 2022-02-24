''' Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequencia de Fibonacci
EX: 0 --> 1 --> 1 --> 3 --> 5 --> 8
Os primeiros números de Fibonacci são:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...
F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 .
 Fn = fn-1 + Fn-2'''

'''
n = int(input('Digite um numero inteiro: '))
cont = 1
nFib1 = 1
nFib2 = 1
soma = 0

print(f'{1} --> {1}', end=' -->')
while cont <= n:
    soma = nFib1 + nFib2
    nFib1 = nFib2
    nFib2 = soma
    print(f' {nFib2}', end=' --> ')
    cont += 1

print('Fim')

 soma = fib1 + fib2;
    fib1 = fib2;
    fib2 = soma;

'''

# Metodo guanabara

n = int(input('Qnts termo voce quer mostrar?: '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} --> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> Fim')


