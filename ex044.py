produto = float(input('Informe o preço do produto: '))
pagamento = float(input('''Informe a condição de pagamento: 
[1] Dinheiro/Cheque. 
[2] Cartão. 
[3] 2x no cartão 
[4] 3x ou mais no cartão
'''))
if pagamento == 1:
    des = produto * 0.1
    valordes = produto - des
    print('O desconto será de 10%, sendo assim R${:.2f} o valor a pagar.'.format(valordes))
elif pagamento == 2:
    des = produto * 0.05
    valordes = produto - des
    print('O desconto será de 5%')
    print('Valor a pagar : R${:.2f}'.format(valordes))
elif pagamento == 3:
    print ('Não há desconto para essa condilão de pagamento, o valor continua R${:.2f}'.format(produto))
elif pagamento == 4:
    juros = produto * 20/100
    valorjur = produto + juros
    print('O produto terá um juros de 20%')
    print('Valor total a pagar: R${:.2f}'.format(valorjur))
else:
    print('Condição inválida. Tenta novamente.')

