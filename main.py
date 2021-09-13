def area(a,b):
    area=a*b
    print(f'A área de um terreno com {a:.2f}x{b:.2f} é igual a {area:.2f}m²')


l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
area(l,c)