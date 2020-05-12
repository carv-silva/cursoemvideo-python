''' Faca um programa que pergunte a distancia de uma viagem em km.Calcule o preco da passagem cobrando R$0.50
por km para viagens de ate 200km e R$0.45 para viajens mais longas''' 

dist = float(input('Entre com a distancia da viagem em Km: '))

'''if dist <= 200:
    t = dist * 0.50
    print(f'O preco total é: R${t:.2f}')
else:
    t = dist * 0.45
    print(f'O preco total é: R${t:.2f}')'''

# segundo metodo

preco = dist * 0.50 if dist <= 200 else dist * 0.45

print(f'O preco total é: R${preco:.2f}')





    