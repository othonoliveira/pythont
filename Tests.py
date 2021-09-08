l=[]
p=[]
i=[]
while True:
    l.append(int(input('Digite um valor: ')))
    r=str(input('Deseja digitar outro valor? [S/N] ')).upper()
    if r=='N':
        break
for c in range(0,len(l)):
    if l[c]%2==0:
        p.append(l[c])
    else:
        i.append(l[c])
print(f'Os valores digitados foram {l}')
print(f'Os valores impares são {i}')
print(f'Os valores pares são {p}')