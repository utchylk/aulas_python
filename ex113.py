def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n1}.')