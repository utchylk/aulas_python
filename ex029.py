vel = float(input('Qual é a velocidade do carro? '))
multa = (vel-80)*7
if vel >80.0:
    print('Você foi multado por ultrapassar o limite de velocidade! O valor a pagar é de R${}.'.format(multa))
else:
    print('Você não foi multado.')