"""Crie um programa que leia o nome  de uma pessoa e diga se ela tem 'Silva' no nome"""

name = str(input('Entre com seu Nome completo: ')).strip()

print(f"Seu nome tem Silva: {'silva' in name.lower()}")
