j={}
gols=[]
j['nome']=str(input('Qual o nome do jogador? '))
j['qjogos']=int(input('Quantas pardidas ele jogou? '))
for g in range(1,j['qjogos']+1):
    gols.append(int(input(f'Quantos gols ele fez na {g}ª partida? ')))
j['gols']=gols[:]
print('-='*30)
print(j)
print('-='*30)
for k,v in j.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {j["nome"]} jogou {j["qjogos"]} partidas')
for g in range(0,j['qjogos']):
    print(f'Na partida {g+1}, fez {j["gols"][g]}')