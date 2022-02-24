'''Crie um programa que leia duas notas de um aluno e calcule sua media
mostrando uma mensagem no final, de acordo com a media atiginda:
1 - Media abaixo de 5.0: Reprovado
2 - Media entre 5.0 e 6.9: Recuperacao
3 - Media entre 7 e superior: Aprovado'''

nota1 = float(input('Entre com a primeira nota de 0 a 10: '))
nota2 = float(input('Entre com a segunda nota de 0 a 10: '))

if nota1 > 10 or nota2 > 10:
    print('Nao sao aceitos valores maior que 10')
    quit()

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua nota é {media}, Aprovado seu nerd...')
elif media < 5:
    print(f'Sua nota é {media}, Voce foi reprovado :( ')
else:
    print(f'Sua nota é {media}, Voce esta de recuperacao, estude mais')


'''Metodo guanabara
if 7> media >=5:
    '''
