l=[]
c=0
while True:
    t=int(input('Digite um valor: '))
    if t in l:
        print(f'O valor {t} está duplicado! Não vou adicionar.')
    else:
        l.append(t)
    r=str(input('Deseja continur? [S/N] ')).upper()
    if r=='N':
        break
print(f'Os valores são {sorted(l)}')