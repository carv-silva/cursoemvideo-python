'''Escreva um porgrama que leia a velocidade de um carro
Se ele ultrapassar  80km/h, mostre uma msg dizendo que ela foi multado
A multa vai custar R$7,00 por cada km acima do limite'''

vel = float(input('Entre com a velocidade, somente numeros: '))

if vel <= 80:
    print('Vc nao ultrapassou o limite de velocidade..')
else:
    multa = (vel - 80) * 7
    print(f'Vc ultrapassou o limite de velocidade sua multa é: R$ {multa}')

### no metodo do guanabara ele nao colocou else