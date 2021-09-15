from tkinter import *

def somar():
    s1=int(n1.get())
    s2=int(n2.get())
    mostrar['text']=s1+s2

root=Tk()

root.geometry('400x400')
root.title('Cadastro')

n1=Entry()
n1.grid(row=0, column=0)

n2=Entry()
n2.grid(row=1, column=0)

Button(text='SOMAR', command=somar).grid(row=2, column=0)

mostrar=Label(text='Resultado')
mostrar.grid(row=3, column=0)

root.mainloop()