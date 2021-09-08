from random import shuffle
l=[]
for c in range(0,5):
    l.append(int(input(f'Digite o {c+1}º valor: ')))
while True:
    if l[0]<l[1]<l[2]<l[3]<l[4]:
        break
    else:
        shuffle(l)
print(f'Os valores em ordem são: {l}')