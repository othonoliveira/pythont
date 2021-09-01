print('Os números pares no intervalo de 1 a 50 são:')
for c in range(0,51,2):
    print(c,end=(''))
    if c==50:
        print('.',end=(''))
    else:
        print(',',end=(''))