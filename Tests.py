p=[]
c=[]
mai=men=0
while True:
    c.append(input('Digite o nome: '))
    c.append(int(input('Digite o peso: ')))
    if len(p)==0:
        mai=men=c[1]
    else:
        if c[1]>mai:
            mai=c[1]
        if c[1]<men:
            men=c[1]
    p.append(c[:])
    c.clear()
    r=str(input('Deseja adicionar outra pessoa? [S/N] ')).upper()
    if r=='N':
        break
print(f'O número de inscrições foi de {len(p)}')
if mai==men:
    print('Os pesos são iguais!')
else:
    print(f'O maior peso foi de {mai}Kg, em ',end='')
    for i in p:
        if i[1]==mai:
            print(f'[{i[0]}]',end='')
    print(f'\nO o menor peso foi de {men}Kg, em ',end='')
    for i in p:
        if i[1]==men:
            print(f'[{i[0]}]',end='')