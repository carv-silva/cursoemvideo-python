'''Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule
seu IMC e mostre seu status de acordo com a tabela abaixo:

1 - Abaixo de 18.5: A baixo do peso
2 - Entre 18.5 e 25: Peso ideial
3 - 25 ate 30: Sobrepeso
4 - 30 ate 40 Obesidade
4 - Acima de 40 : morbida, vc vai morrer
IMC = Peso ÷ (Altura × Altura)'''

peso = float(input('Entre com seu Peso(kg): '))
altura = float(input('Entre com seu Altura (metro e cm): '))

imc = peso / (altura ** 2)
print('O seu IMC é: {:.2f}'.format(imc))


if imc > 40:
    print('Morbida(o), vc vai morrer :/')
elif 18.5 <= imc < 25:
    print('Peso ideial, Garoto saude :)')
elif 25 <= imc < 30:
    print('Sobrepeso, vai correr seu gordo')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('A baixo do peso :( vai comer feijao...')





