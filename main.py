a=[]
l=[]
while True:
    l.append(str(input('Nome: ').capitalize()))
    l.append(float(input('Nota 1: ')))
    l.append(float(input('Nota 2: ')))
    a.append(l[:])
    t=str(input('Deseja continuar? [S/N] ')).upper()
    if t=='N':
        break
    l.clear()
print('Boletim'.center(30,'-'))
for c in range(0,len(a)):
    print(f'{c+1}.{a[c][0]} média {((a[c][1])+(a[c][2]))/2:.2f}')
while True:
    t=str(input('Deseja ver a nota de algum aluno? [S/N] ')).upper()
    if t=='S':
        t=int(input('Digite o número do aluno: '))
        print(f'As notas de {a[t-1][0]} são n1:{a[t-1][1]:.2f} e n2:{a[t-1][2]:.2f}')
    if t=='N':
        break
