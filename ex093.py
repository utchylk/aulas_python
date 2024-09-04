lista = {}
lista['nome'] = str(input('Nome: '))
partidas = list()
part = int(input(f'Quantas partidas {lista['nome']} jogou? '))
for c in range(0, part):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
lista['gols'] = partidas[:]
lista['total'] = sum(partidas)
print(lista)
print('-'*30)
for k, v in lista.items():
    print(f'O campo {k} tem valor {v}')
print('-'*30)
print(f'O jogador {lista['nome']} jogou {part} partida(s).')
for i, v in enumerate(lista['gols']):
    print(f'=>Na partida {i} fez {v} gols')
print(f'Foi um total de {lista['total']} gols.')