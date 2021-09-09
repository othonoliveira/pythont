l=[[],[],[]]
s=mai=t=0
for i in range(0,3):
    for c in range(0,3):
        l[c].append(int(input(f'Digite o valor para [{i},{c}]: ')))
for i in range(0,3):
    for c in range(0,3):
        if l[i][c] % 2==0:
            s+=l[i][c]
        if c==2:
            t+=l[i][c]
        if i==1 and l[i][c]>mai:
            mai=l[i][c]
print('-='*30)
print('',l[0],'\n',l[1],'\n',l[2],)
print('-='*30)
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da 3º coluna é {t}')
print(f'O maior valor da 2º linha é {mai}')