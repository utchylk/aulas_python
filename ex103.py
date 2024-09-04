def ficha(a=0, b=0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato')


jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(b=gols)
else:
    ficha(jogador, gols)