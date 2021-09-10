a={}
a['nome']=str(input('Digite o nome do aluno: '))
a['media']=float(input('Digite a média do aluno: '))
if 5<=a['media']<7:
    a['situação']='Recuperação'
if a['media']>=7:
    a['situação']='Aprovado'
if a['media']<5:
    a['situação']='Reprovado'
print(f'O aluno {a["nome"]} foi {a["situação"]}')