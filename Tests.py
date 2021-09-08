p=[]
c=[]
while True:
    c.append(input('Digite o nome: '))
    c.append(input('Digite o peso: '))
    p.append(c[:])
    c.clear()
    r=str(input('Deseja adicionar outra pessoa? [S/N] ')).upper()
    if r=='N':
        break
print(p)