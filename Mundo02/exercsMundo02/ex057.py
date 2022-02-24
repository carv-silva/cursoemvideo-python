'''Faça um programa que leia o sexo de uma pessoa, mais so aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação novamente ate ter um valor correto.'''

'''
r = 'S'
p = 'M'

while p == 'M' or p == 'F' or r == 'S':
    p = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if p == 'M':
        print('Seu sexo é masculino')
        exit()
    elif p == 'F':
        print('Seu sexo é feminino')
        exit()
    else:
        print("Digite seu sexo corretamente com 'M' ou 'F' ")
print('Fim')'''



''' Metodo guanabara'''

sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F]')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
#




