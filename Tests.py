from random import shuffle
lista=[]
for c in range(1,8):
    n=float(input('Digite o peso da {}º pessoa: '.format(c)))
    lista.append(n)
c=0
while c==0:
    if lista[0]<lista[1]<lista[2]<lista[3]<lista[4]<lista[5]<lista[6]:
        print('O maior peso foi de {}'.format(lista[6]),'\nO menor peso foi de {}'.format(lista[0]))
        c=1
    else:
        shuffle(lista)
