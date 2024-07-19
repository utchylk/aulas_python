sal = int(input('Qual o seu salário? '))
if sal > 1250:
    aumento = sal*0.1
    sal2 = sal+aumento
    print('Você vai receber um aumento de 10%, ficando assim R${}.'.format(sal2))
else:
    aumento = sal*0.15
    sal2 = sal+aumento
    print('Você vai receber um aumento de 15%, ficando assim com um salário de R${}.'.format(sal2))
