"""Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome 'Santo'"""

cdd = str(input('Entre com uma cidade: ')).strip() ## --> ja le a entrada e remove os espaco
print(cdd[:5].lower() == 'santo')
