lanche = ('hambuerguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche)
print(lanche[1])
print(lanche[2:])
print(lanche[-1])
print(lanche[-2])
print(lanche[:2])
# do inicio ate o elemnto 2 e ingora o 2
print(lanche[-2:]) # --> do penultimo ate o ultimo

# formatando a tupla com estilo

for comida in lanche:
    print(f'Eu vou comer a comida {comida}')

# outra maneira de usar o for para percorrer a tupla:

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posicção {cont}')

    # outra forma de percorrer nao muito usada

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer a comida {comida} na posição {pos}')

# forma de organizar a tupla em ordem alfabetica

print(sorted(lanche))

# somandos as duas tuplas completa
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# ordenando

print(sorted(c))

# a ordem importa nas tuplas

# tamanho de elementos e metodos
print(len(c))

print(c.count(5)) # qnts vezes o numero 5 aparece ?
print(c.index(8)) # em que posição esta o numero 8? R: 1
print(c.index(4))  # em que posição esta o numero 4? R: 6
print(c.index(2, 4))  # aqui ele vai pega começas a contar a partir da posição 4 e pega o que ta na posição 2

pessoa = ('Gustavo', 39, 'M', 99.88) # misturando string com int e float
del(pessoa) # apesar de tuplas é imutavel, podemos apagar ela aqui
