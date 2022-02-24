'''Aula13 lacos de repitiçoes
for c in rage(1,10): --> fazer o contator c no intervo de 1 a 10 '''

'''for i in range(0, 6): # --> conta pra frente, se quiser decrecente
 so colar -1
 EX:for i in range(7, 0, -1):

# o terceiro digito é a interação que vc quer no laço:
EX for i in range(0, 6, 2): --> ELE VAI CONTAR DE 0 A 5 PULANDO 2 CASA
 '''

'''for i in range(10, 6, -1):
    print(i)
print('OI fim')'''
'''

n = int(input('Digite um numero: '))

for i in range(0, n + 1):
    print(i)
print('Fim')'''

'''
i = int(input('Inicio: '))
f = int(input('FIm: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):
    print(c)
print('Fim')
'''

s = 0
for c in range(0, 4):
    n = int(input('Entre com uma valor: '))
    s += n
print(f'O somatorio de todos os valores foi: {s}')
