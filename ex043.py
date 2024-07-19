peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/altura**2
if imc < 18.5:
    print('\033[34mAbaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('\033[34mPeso ideal')
elif imc >= 25 and imc <30:
    print('\033[34mSobrepeso')
elif imc >= 30 and imc < 40:
    print('\033[34mObesidade')
else:
    print('\033[34mObesidade mórbida')

