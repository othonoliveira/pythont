f=str(input('Digite uma expressão: '))
l=[]
for i in f:
    if i=='(':
        l.append('(')
    elif i==')':
        if len(l)>0:
            l.pop()
        else:
            break
if len(l)==0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')