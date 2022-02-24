from datetime import date
'''Faca um programa que leia o ano de nascimento de um jovem e informe, de
acordo com sua idade
1 - Se ele ainda vai se alistar no serviço militar
2 - Se é a hora de ele se alistar
3 - Se ja passou do tempo do alistamento

seu programa tambem devera mostrar o tempo que falta ou que passou do prazo'''

print(
    '''=====\033[34m Bem vindo ao verificador de alistamento militar ''' +
    ''' \033[m====  ''')

print('''
    [1] Masculino
    [2] Feminino
    [3] Sair do Programa
    ''')


escolha = int(input('Escolha seu sexo: '))

if escolha == 1:

    dataAtual = date.today().year
    anoNasc = int(input('Entre com a data de nascimento: '))
    idade = dataAtual - anoNasc

    if anoNasc > dataAtual:
        print('O ano de nascimento nao pode ser maior que o atual')

    print(f'Quem nasceu em {anoNasc} tem {idade} anos em {dataAtual}')

    if idade < 18:
        print(f'Sua idade é {idade}, ainda falta: {18 - idade} anos ', end='')
        print('para vc se alistar')
        print(f'Seu ano de alistamento sera em: {anoNasc + 18}')
    elif idade == 18:
        print(f'Sua idade é {idade}, esse ano {dataAtual} vc tem que se alistar')
    else:
        print(f'Sua idade é {idade}')
        print(f'Vc deveria ter se alistado ha: {idade - 18 } anos')
        print(f'Seu ano de alistamento foi: {dataAtual - (idade - 18 )}')

elif escolha == 2:
    print('Voce nao precisa se alista :) ')

elif escolha == 3:
    exit()

else:
    print('Escolha uma opção valida...')

