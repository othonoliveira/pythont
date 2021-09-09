l=[[],[]]
for c in range(0,7):
    r=int(input(f'Digite o {c+1}º valor: '))
    if r%2==0:
        l[0].append(r)
    else:
        l[1].append(r)
print(f'Os números pares são {sorted(l[0])}')
print(f'Os números impares são {sorted(l[1])}')