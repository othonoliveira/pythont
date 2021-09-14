def voto(a):
    from datetime import datetime
    r=datetime.now().year-a
    return r


a=int(input('Digite o ano de nascimento: '))
r=voto(a)
if r>=18:
    print('Voto OBRIGATÓRIO')
if r<18 and r>=16:
    print('Voto OPCIONAL')
if r<16:
    print('Voto NEGADO')