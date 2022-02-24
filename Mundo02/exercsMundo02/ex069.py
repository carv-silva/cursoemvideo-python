'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa
cadastrada, o
programa devera pergutar se o usuario quer ou nao continuar. No final mostre:

A) qnts pessoas tem mais de 18 anos.
B) qnts homens foram cadastrados.
C) qnts mulheres tem menos de 20 anos'''

somaPessoa = somaHomem = somaMulher = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]

    if sexo == 'M':
        somaHomem += 1

    if idade >= 18:
        somaPessoa += 1

    if sexo == 'F' and idade < 20:
        somaMulher += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break


print(f'A quantidade de pessoas que tem mais de 18 é: {somaPessoa}')
print(f'A quantidade de Homens  cadastrado é: {somaHomem}')
print(f'A quantidade de mulheres menores de 20 anos é: {somaMulher}')
