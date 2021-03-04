nome = str(input('Qual é seu nome gostozao? '))
if nome == 'Carlao':
    print('Que nome lindao')
elif nome == 'Cavalo' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino!!')
else:
    print('Seu nome é bem normal!!')
print(f'Tenha um bom dia {nome}')

# print(f'Tenha um bom dia: {nome}')
