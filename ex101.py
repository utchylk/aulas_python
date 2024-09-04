def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return(f'Com {idade} anos: VOTO NEGADO')
    elif idade >= 18 and idade < 65:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 16 and idade < 18 or idade > 65:
        return(f'Com {idade} anos: VOTO OPCIONAL')


print('-'*30)
anos = int(input('Em que ano você nasceu? '))
print(voto(anos))

