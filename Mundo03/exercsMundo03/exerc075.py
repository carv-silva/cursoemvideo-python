'''Desenvolva um programa que leia quatros valores pelo teclado e
guarde-os em uma tupla. No final mostre:
A) quantos vezes aparece o valor 9.
B) em que posição foi digitado o primeiro valor 3
C) quais foram os numeros pares.'''


tupla = tuple(int(input('Digite um numero: '))for i in range(0, 4))
print(tupla)

print(f'O valor 9 aparece {tupla.count(9)}vezes')
if (3 in tupla) == True:
    print(f'O valor 3 aparece na {tupla.index(3) + 1 } Posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')

for i in tupla:
    if i % 2 == 0:
        lista = []
        lista.append(i)
        for pares in lista:
            if pares != None:
                lista_pares = []
                lista_pares.append(pares)
                lista_pares_format = *lista_pares, sep=','
                print(f"Os valores pares digitados sao:{lista_pares_format}")
                #lista_pares_format = "".join(map(str,lista_pares))
                #print(lista_pares_format, end=',')
            
        #lista.append(pares).join(map(int, lista))
        #lista = "".join(map(str, lista)
        #print(lista)
        #print(tuple(tupla))
        #print(f'Os valores pares digitados sao: {pares}') 
        