from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)
        }
ranking = list()
print('Valores sorteados: ')
for j, t in dado.items():
    print(f'{j} tirou {t} no dado')
    sleep(1)
print('RANKING DOS JOGADORES')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]} pontos')

