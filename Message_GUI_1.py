import tkinter as tk
from tkinter import *


def _quit():
    win_message.quit()
    win_message.destroy()


def postiv_message():
    global win_message
    win_message = tk.Tk()
    win_message.geometry("350x150+500+300")
    win_message.config(background='#CCB4B2')
    win_message.resizable(0, 0)
    win_message.title("Résultat de prédiction")
    intro = Message(win_message, justify=CENTER, width=300, font=("Gill Sans", 15, 'bold'), bg='#CCB4B2', text=" Le patient a une maladie cardiovasculaire")
    intro.place(x=35, y=20)
    check_button = Button(win_message, text='Confiremer ', font=("Gill Sans", 12, 'bold'), bg='#A40D00', fg='white', cursor="hand2", borderwidth='4', relief=RAISED, command=_quit)
    check_button.place(x=120, y=100)
    win_message.mainloop()
