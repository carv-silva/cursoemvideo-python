"""Faca um programa que leia  uam frase pelo teclado e mostre

qnts vez aparece a letra a

em que posicao ela aparece a primeira vez

em que posicao ela aparece pela ultima vez"""

frase = str(input('Escreva algo: ')).lower().strip()

print(f"A frase tem: { frase.count('a')}")
print(f"A primeira posicao que aparece é: {frase.find('a') + 1}")
print(f"A ultima  posicao é: {frase.rfind('a') + 1}")


