l=[]
for c in range(0,5):
    l.append(int(input(f'Digite um número para a posição {c}: ')))
print(f'Você digitou os valores: {l}')
if l[0]==l[1]==l[2]==l[3]==l[4]:
    print('Todos os valores são iguais!')
else:
    print(f'O maior valor digitado foi {max(l)} nas posições ',end='')
    for c in range(0,5):
        if max(l)==l[c]:
            print(f'{c}...',end='')
    print(f'\nO menor valor digitado foi {min(l)} nas posições ',end='')
    for c in range(0,5):
        if min(l)==l[c]:
            print(f'{c}...',end='')