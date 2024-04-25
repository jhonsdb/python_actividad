""" importamos la librerias que  necesitamos """
from tkinter import *
from tkinter import ttk
import math

root= TK()
root.title("calculadora")
root.geometry("500+80")


mainframe = ttk.Frame(root)
mainframe.grid(column=0,row=0)

entrada1=StringVar
label_entrada1=ttk.label(mainframe,textvariable=entrada1) 