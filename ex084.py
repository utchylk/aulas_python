pessoas = list()
galera = list()
pes = lev = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append((float(input('Peso: '))))
    if len(galera) == 0:
        pes = pessoas[1]
        lev = pessoas[1]
    else:
        if pessoas[1] > pes:
            pes = pessoas[1]
        if pessoas[1] < lev:
            lev = pessoas[1]
    r = str(input('Quer continuar? [S/N]: '))
    galera.append(pessoas[:])
    pessoas.clear()
    if r in 'Nn':
        break
print(f'Foram registradas {len(galera)} pessoas.')
print(f'O maior peso foi de {pes}kg.', end=' ')
for p in galera:
    if p[1] == pes:
        print(f'Peso de {p[0]}')
print(f'O menor peso foi de {lev}kg.', end=' ')
for p in galera:
    if p[1] == lev:
        print(f'Peso de {p[0]}')

