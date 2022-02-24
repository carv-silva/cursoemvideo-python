'''Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas.No final do programa mostre:

A media de idade do grupo:
Qual é o nome do homem mais velho.
Quantas mulheres tem menos que 20 anos'''

nome = []
idade = []
sexo = []
totMulher20 = 0

for i in range(1, 5):
    print(f'-----{i}ª Pessoa ----- ')
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    sexo.append(input('Sexo: [M/F]:'))
    print('=' * 25)

media = sum(idade) / len(idade)
maiorIdade = max(idade)
nomeMaisVelho = idade.index(maiorIdade)

'''if sexo in 'Ff' and idade < 20:
        totMulher20 += 1'''

print(f'A media de idade das pessoas sao: {media}')
print(f'O homem mais velho é {nome[nomeMaisVelho]} com {maiorIdade} anos')


'''
# ---- metodo guanabara ----

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0


for p in range(1, 5):
    print(f'-----{p}ª Pessoa ----- ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]:')).strip()
    somaIdade += idade
    print('=' * 25)

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade / 4
print(f'A media de idade é de: {mediaIdade}')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo sao {totMulher20} mulheres com menos de 20 anos')
'''
