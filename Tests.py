l=[[],[],[]]
for i in range(0,3):
    for c in range(0,3):
        l[c].append(int(input(f'Digite o valor para [{i},{c}]: ')))
print('-='*30)
print('',l[0],'\n',l[1],'\n',l[2],)