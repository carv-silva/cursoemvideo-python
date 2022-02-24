''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condiçao de pagamento:
1 -  A vista dinhero / cheque: 10% de desconto
2 - A vista no cartao: 5%
3 - em ate 2x no cartao: preço normal
4 - 3x ou mais no cartao: 20 %  de juros'''

# print('''=====\033[34m \ Loja do Carlao / \033[m====
# ''')

print('{:=^40}'.format(' \033[34m Loja do carlao \033[m '))


# print('\033[30m Hello thanks! \033[m')
precoProduto = float(input(' \nTotal das compras: '))
print('''

    [1] À VISTA Dinheiro/Cheque 10% de desconto.
    [2] À Vista Cartão 5% de desconto.
    [3] 2 X no Cartão
    [4] 3 X ou mais no Cartão
    [5] Sair do Programa
    ''')

formaDePagamento = float(input('Escolha a forma de pagamento: '))

dinheiroCheque = precoProduto - ((10 * precoProduto) / 100)
avistaCartao = precoProduto - ((5 * precoProduto) / 100)
parceladoDuasVez = precoProduto / 2

if formaDePagamento == 1:
    print(f'Valor: {precoProduto} \nTotal com desconto R$: {dinheiroCheque}')
elif formaDePagamento == 2:
    print(f'Valor: {precoProduto} \nTotal com desconto R$: {avistaCartao}')
elif formaDePagamento == 3:
    print(f'Valor: {precoProduto} \n Valores da parcela R$: {parceladoDuasVez}')
elif formaDePagamento == 4:
    parcelado = float(input('Digite a quantidade de parcelas: '))
    if parcelado > 2:
        # print(f'Valor: {precoProduto} \n Valores da parcela:', end='')
        parcelaTotal = ((precoProduto * 20 / 100) + precoProduto) / parcelado
        print(f'A parcela com juros é {parcelado}x de R$:{parcelaTotal}')
    else:
        print('Caso vc deseja parcelar em 2x Escolha a opc 3 do Menu ')
elif formaDePagamento == 5:
    exit()
else:
    print('Opcao invalida, Favor escolher uma valida!!!')

