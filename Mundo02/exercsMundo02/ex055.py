''' Faca um programa que leia o peso de 5 pessoas
No final, mostre qual foi o maior e o menor peso lido'''

lista = []
for i in range(1, 6):
    lista.append(float(input('Entre com seu peso em KG: ')))

print(f'O maior peso da lista digitado é: {max(lista)}')
print(f'O menor peso da lista digitado é: {min(lista)}')
 



