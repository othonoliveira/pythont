from time import sleep
from random import randint
s=[]
print('-'*30)
print('Joga na MEGA SENA'.center(30,' '))
print('-'*30)
q=int(input('Quantos jogos quer que eu sortei? '))
print(f'Soteando {q} jogos'.center(30,' '))
for c in range(0,q):
    for i in range(0,6):
        s.append(randint(1,60))
    sleep(1)
    print(f'Jogo {c+1}: {sorted(s)}')
    s.clear()