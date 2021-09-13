from random import randint
from time import sleep

def sort():
    print('Sorteando os números: ', end='')
    for c in range(0,5):
        sleep(1)
        num.append(randint(0,100))
        print(num[c], end=' ', flush=True)



def somapar():
    s=0
    for c in range(0,5):
        if num[c]%2==0:
            s+=num[c]
    return(s)


num=[]
sort()
print(f'\nA soma dos números pares é: {somapar()}')