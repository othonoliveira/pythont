from operator import itemgetter
j={}
p=[]
m=[]
id=[]
si=0
while True:
    j['Nome']=str(input('Nome: ')).capitalize()
    j['Sexo']=str(input('Sexo:[M/F] ')).upper()
    j['Idade']=int(input('Idade: '))
    si+=j['Idade']
    id.append(j.get('Idade'))
    print(id)
    if j['Sexo']=='F':
        m.append(j.copy())
    p.append(j.copy())
    j.clear
    t=str(input('Deseja adicionar outra pessoa?[S/N] ')).upper()
    if t=='N':
        break
si=si/len(p)
print(f'Foram cadastras {len(p)} pessoas.')
print(f'A média das idades é {si:.2f}')
print(f'As mulheres cadastradas foram {m}')
print(f'As pessoas com idade maior q a média são ',end='')
for c in range(0,len(id)):
    if id[c]>si:
        print(p[c],end=' ')