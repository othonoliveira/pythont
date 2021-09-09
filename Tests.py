l=[]
p=[]
i=[]
for c in range(0,7):
    r=int(input(f'Digite o {c+1}º valor: '))
    if r%2==0:
        p.append(r)
    else:
        i.append(r)
l.append(p[:])
l.append(i[:])
print(f'Os números pares são {l[0]}')
print(f'Os números impares são {l[1]}')