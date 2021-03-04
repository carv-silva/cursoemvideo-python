'''if carro.esquerda():
    bloco True
else:
    bloco Flase'''


'''tempo = int(input('Qual o tempo do seu carro? '))

if tempo <=3:
    print('Seu carro esta novo')
else:
    print('Seu carro esta velho') 
print('Fim :)')    

## 2 metodo simplificado :)

tempo = int(input('Qual o tempo do seu carro? '))
    print('Carro Novo' if tempo<=3 else 'Carro velho')
print('Fim :)')  

name = str(input('Entre com um nome: ')).lower()

if name == 'carlos':
    print('Que nome tzao vc tem')
else:
    print(f'Bom dia, {name}')
'''

n1 = float(input('Entre com a nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2) / 2

if m >= 6.0:
    print(f'Sua nota é {m:.1f}')
    print('Aprovado')
else:
    print(f'Sua nota é {m:.1f}')
    print('Reprovado')

##Versao simplificada

n1 = float(input('Entre com a nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2) / 2

print(f'Sua nota é {m:.1f}')
print('Aprovado' if m >=6 else 'Reprovado')