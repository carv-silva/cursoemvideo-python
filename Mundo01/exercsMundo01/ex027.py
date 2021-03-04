"""Faca um programa que leia um nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
ex: Ana Maria de souza
primeiro = Ana
ultimo = souza"""

n = str(input('Entre com seu Nome completo: ')).strip().title()
n = n.split()
print(f"O primeiro nome dela é: {n[0]} e o ultimo nome é: {n[len(n) -1]}")



