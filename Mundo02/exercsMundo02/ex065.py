'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a
a media da execução, mostre a media entre todos os valores e qual foi o menor e o maior valores lidos
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores'''

'''
r = 'S'
lista = []

while r == 'S':
    number = int(input('Digite um numero inteiro aleatorio: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    lista.append(number)

#media = sum(lista) / len(lista)
menor = min(lista)
maior = max(lista)
print(f'Voce digitou {len(lista)} numeros')
print(f'A media dos valores foi:{sum(lista) / len(lista)}')
print(f'O menor numero digitado foi: {menor} e o maior é: {maior}')'''



# metodo guanabara


resp = 'S'
soma = qnt = media = 0

while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    qnt += 1
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior - n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / qnt
print(f'Voce digitou {qnt} numeros e a media é {format(media)}')
print(f'O maior é {maior} e o menor é {menor}')
print('Acabou')


