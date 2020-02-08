'''Crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas letras  maiscula
o nome com todas letras minuscula
quantas letras  ao todo sem considerar os espaco
qnts letrastem o primeiro nome
'''


nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print(f'Seu nome em maisculo é:{nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f"Seu primeiro nome tem o total de {len(nome) -nome.count(' ')} letras")
#print(f"O primeiro nome tem: {nome.find(' ')}")
nome_list = nome.split()
print(f'Seu primeiro nome é:{nome_list[0]} e tem o total de {len(nome_list[0])} letras')