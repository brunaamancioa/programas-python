from tkinter import *
from tkinter import ttk
from turtle import width

#Cores

cor1 = "#444466"
cor2 = "#feffff"
cor3 = "#008000"

window = Tk()
window.title('')
window.geometry('320x220')
window.resizable(height=FALSE, width=FALSE)
window.configure(bg=cor2)

frameTopo = Frame(window,width=295,height=50,bg=cor2,pady=0,padx=0)
frameTopo.grid(row=0,column=0)

frameBaixo = Frame(window,width=295,height=50,bg=cor2,pady=0,padx=0)
frameBaixo.grid(row=1,column=0)

nomePrograma = Label(frameTopo,text='Calculadora IMC',width=26,height=1,padx=0,anchor="center",font=('Arial'),bg=cor2,fg=cor1)
nomePrograma.place(x=0,y=2)

linePrograma = Label(frameTopo,text='',width=400,height=1,padx=0,anchor="center",font=('Arial 20'),bg=cor3,fg=cor1)
linePrograma.place(x=0,y=40)

def calcular():
    peso = float (ePeso.get())
    altura = float (eAltura.get()) ** 2
    resultado = peso / altura

    if resultado < 18.4:
        lineResultado_texto['text'] = "Seu IMC é: Abaixo do Peso"
    elif resultado >= 18.5 and resultado < 24.9:
        lineResultado_texto['text'] = "Seu IMC é: Normal"
    elif resultado >= 25 and resultado < 29.9:
        lineResultado_texto['text'] = "Seu IMC é: Sobrepeso"
    else:
        lineResultado_texto['text'] = "Seu IMC é: Obesidade"
    
    lineResultado['text'] = "{:.{}f}".format(resultado,2)
    
linePeso = Label(frameBaixo,text='Digite seu peso: ', height=1, padx=0,anchor='center',font=('Arial 13'),bg=cor2,fg=cor1)
linePeso.grid(row=0,column=0, columnspan=1,pady=2,padx=0)
ePeso=Entry(frameBaixo,width=5,font=('Arial'),justify='center',relief=SOLID)
ePeso.grid(row=0,column=1,columnspan=1,pady=10,padx=3)

lineAltura = Label(frameBaixo,text='Digite sua altura: ', height=1, padx=0,anchor='center',font=('Arial 13'),bg=cor2,fg=cor1)
lineAltura.grid(row=1,column=0, columnspan=1,pady=10,padx=3)
eAltura=Entry(frameBaixo,width=5,font=('Arial'),justify='center',relief=SOLID)
eAltura.grid(row=1,column=1,columnspan=1,pady=10,padx=3)

lineResultado = Label(frameBaixo,width=5,text="----",height=1,padx=15,pady=20,anchor='center',font=('Arial'),bg=cor3,fg=cor2)
lineResultado.place(x=220,y=16)

lineResultado_texto = Label(frameBaixo,width=37,text="",height=1,padx=6,pady=12,anchor='center',font=('Arial 10'),bg=cor2,fg=cor1)
lineResultado_texto.place(x=0,y=85)

botaoCalcular=Button(frameBaixo,text='Calcular',width=32,height=1,bg=cor3,fg=cor2,font=('Arial 13'),anchor='center',command=calcular)
botaoCalcular.grid(row=4,column=0, pady=30,padx=5,columnspan=30)

window.mainloop()

