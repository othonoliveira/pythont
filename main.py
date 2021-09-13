from time import sleep
def cont(init,fim,pas):
    if init>fim:
        con=init
        while cont<=fim:
            print(f'{con}', end=' ', flush=True)
            con+=pas
            sleep(0.5)
        print('Fim!')
    else:
        con=init
        while con<=fim:
            print(f'{con}', end=' ', flush=True)
            con-=pas
            sleep(0.5)
        print('Fim!')


cont(-10,-8,-2)