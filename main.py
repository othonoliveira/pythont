def fat(a,b=bool()):
    r=1
    if a==1:
        print(f'O reultado é: {a}')
    elif b==False:
        for c in range(1,a+1):
            r*=c
        print(f'O resultado é: {r}')
    elif b==True:
        for c in range(a,0,-1):
            r*=c
            if c!=1:
                print(f'{c} X', end=' ')
            if c==1:
                print(f'1 = {r}')


f=int(input('Digite um número: '))
fat(f, True)