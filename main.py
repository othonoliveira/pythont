from random import randint
from operator import itemgetter
from time import sleep
j={'Jogador 1': int(randint(1,6)),'Jogador 2': int(randint(1,7)),'Jogador 3': int(randint(1,7)),'Jogador 4': int(randint(1,7))}
r=dict()
c=1
for i,n in j.items():
    print(f'O {i} tirou {n}.')
    sleep(1)
print('-'*30)
r=sorted(j.items(), key=itemgetter(1), reverse=True)
for i,n in r:
    print(f'{c}º lugar: {i} com {n}')
    sleep(1)
    c+=1