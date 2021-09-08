l=[]
while True:
    l.append(int(input('Digite um valor: ')))
    r=str(input('Deseja digitar outro valor? [S/N] ')).upper()
    if r=='N':
        break
print(f'Foram digitado {len(l)} números.')

print(f'Os números em ordem decrescente são {sorted(l,reverse=True)}.')
if l.count(5)!=0:
    print(f'O número 5 aparece {l.count(5)} vezes')