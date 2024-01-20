
from tkinter import *
import tkinter
from datetime import datetime

import pyglet 
pyglet.font.add_file('digital-7.ttf')

cor1 = '#3d3d3d' #preto
cor2 = '#ffffff' #branco
cor3 = '#e57d90' #rosa
cor4 = '#967491' #lilás
cor5 = '#779ECB' #azul

fundo = cor1
cor = cor3

janela = Tk()
janela.title('')
janela.geometry('400x180')
janela.resizable(width=FALSE,height=FALSE)
janela.configure(bg=cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    diaSemana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')
    
    linha1.config(text=hora)
    linha1.after(200, relogio)
    linha2.config(text=diaSemana + '  ' + str(dia) + '/' + str(mes) + '/' + str(ano))


linha1 = Label(janela,text='',font=('digital-7 100'),bg=fundo,fg=cor)
linha1.grid(row=0,column=0,sticky=NW,padx=5)

linha2 = Label(janela,text='',font=('digital-7 17'),bg=fundo,fg=cor)
linha2.grid(row=1,column=0,sticky=NW,padx=5)

relogio()


janela.mainloop()
