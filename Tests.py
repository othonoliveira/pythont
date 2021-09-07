t=(int(input('Digite o 1º número: ')),int(input('Digite o 2º número: ')),int(input('Digite o 3º número: ')),int(input('Digite o 4º número: ')))
print(f'O número 9 aparece {t.count(9)}')
print(f'O primeiro falor 3 foi digitado na posição {t.index(3)+1}')
for n in t:
    if n%2==0:
        print(f'Os números pares são:{n}',end=' ')