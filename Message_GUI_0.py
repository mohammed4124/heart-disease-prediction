import tkinter as tk
from tkinter import *


def _quit():
        win_message.quit()
        win_message.destroy()



def negativ_message():
        global win_message
        win_message = tk.Tk()
        win_message.geometry("350x150+500+300")
        win_message.config(background='#B2FCD8')
        win_message.resizable(0, 0)
        win_message.title("Résultat de prédiction")
        intro = Message(win_message, justify=CENTER, width=300, font=("Gill Sans", 15, 'bold'), bg='#B2FCD8', text=" Le patient n'a pas une maladie cardiovasculaire")
        intro.place(x=18, y=20)
        check_button = Button(win_message, text='Confiremer ', font=("Gill Sans", 12, 'bold'), bg='#027B40', fg='white', cursor="hand2", borderwidth='4', relief=RAISED, command=_quit)
        check_button.place(x=120, y=100)
        win_message.mainloop()
