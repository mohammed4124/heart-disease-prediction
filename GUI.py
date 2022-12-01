from application import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Menu, ttk
import pandas as pd

import Message_GUI_0
import Message_GUI_1


df = pd.read_csv('dataset.csv')
test_values = [[]]
texts = []
positiv_msg = Message_GUI_1
negativ_msg = Message_GUI_0

def alert():
    negativ_msg.negativ_message()


def test_gui():
    #test(get_text())
    pass


def _quit():
    win.quit()
    win.destroy()
    exit()


def get_text():
    for text in texts:
        test_values[0].append(text.get())


def check_empty():
    index = 0
    for text in texts:
        index = index + 1
        if len(text.get()) == 0:
            text.config({"background": "#F7948D"})
        else:
            check_type(index, text.get())

comboboxvalues={"Homme":1,"Femme":0,"Angine typique":0,"Angine atypique":1,"Douleur non angineuse":2,"Asymptomatique":3,"Normal":0,"Anomalie de ST-T":1,"Hypertrophie ventriculaire gauche":2,"Non":0,"Oui":1,"Montant":0,"Plat":1,"Descendant":2}
echontillon=[]
def check_type(i, t):
    j = ["Age", "Sex", "Douleur thoracique", "Tension artérielle", "Cholestérol", "Glycémie à jeun", "ECG", "Fréquence cardiaque max", "Angine par l'effort", "Dépression ST", "Pente du segment ST", "Nb de gros vaisseaux", "Thalassémie"]
    if i in [2, 3, 7, 9, 11]:
        if texts[i].get() in comboboxvalues:
            echontillon.append(comboboxvalues.get(texts[i].get()))

    else:
        try:
            echontillon.append(float(t))
        except ValueError:
            messagebox.showerror(j[i-1]," Doit etre numérique. Refomuler la SVP !" )
    if len(echontillon) == 13:
        echontillon.append(1)
        if test(processing_test_value(echontillon)) == [0]:
            positiv_msg.postiv_message()
        else:
            negativ_msg.negativ_message()


def clear_text():
    index = 0
    for text in texts:
        index = index+1
        if index in [2, 3, 7, 9, 11]:
           pass
        else:
            text.delete(0, 'end')
            text.config({"background": "white"})


def main():
    global win
    win = tk.Tk()
    win.geometry("800x500+300+100")
    win.resizable(0, 0)
    win.title("Prédicteur de maladie cardiaque")
    icon = PhotoImage(file='heart.png')
    win.iconphoto(True, icon)
    photo = PhotoImage(file="back_button1.png")
    button_photo = photo.subsample(10, 10)
    # win.config(background='')

    # Exit action

    # Create Menu Bar
    menuBar = Menu(win)
    win.config(menu=menuBar)

    # Menu Option
    def show_about():
        about.tkraise()

    def show_home():
        isolateur.tkraise()
        home.tkraise()
    def show_msg():
        messagebox.showinfo("Message", "Hey There! I hope you are doing well.")


    '''fileMenu = Menu(menuBar, tearoff=0, bg='white', activebackground='#155994', activeforeground='white' ,font=("Gill Sans", 10))
    autreMenu = Menu(menuBar, tearoff=0, bg='white', activebackground='#155994', activeforeground='white', font=("Gill Sans", 10))
    fileMenu.add_cascade(label='Autres', menu=autreMenu, font=("Gill Sans", 10))
    autreMenu.add_command(label="à propos", command=show_about)
    autreMenu.add_command(label="Contacts")
    fileMenu.add_separator()
    fileMenu.add_command(label="La carte thermique", command=plot_heat_map)
    fileMenu.add_separator()
    fileMenu.add_command(label="Histogramme", command=plot_histogram)
    fileMenu.add_separator()
    fileMenu.add_command(label="Ratios de patients", command=plot_patient_num)
    fileMenu.add_separator()
    fileMenu.add_command(label="Fermer", command=_quit)
    menuBar.add_cascade(label="Options", menu=fileMenu, font=("Gill Sans", 10))'''

    # Menu Aider

    aiderMenu = Menu(menuBar, tearoff=0, bg='white', activebackground='#155994', activeforeground='white', font=("Gill Sans", 10, 'bold'))
    #aiderMenu.add_command(label="KNN scores", command=plot_knn_scores)
    aiderMenu.add_command(label="à propos", command=show_about)
    aiderMenu.add_separator()
    aiderMenu.add_command(label="guide d'étulisation", state=DISABLED)
    aiderMenu.add_separator()
    aiderMenu.add_command(label="Fermer", command=_quit)
    menuBar.add_cascade(label=" Aider ?", menu=aiderMenu)

    # Introduction label

    # about
    about = Frame(win, bg='#6FE2FA', height=500, width=800)
    about.place(x=0, y=0)
    back_button = Button(about, image=button_photo, bd=0, bg='#6FE2FA', activebackground="#6FE2FA", cursor="hand2", command=show_home)
    back_button.place(x=5, y=5)

    title1 = Label(about, text="à propos:", bg='#6FE2FA', font=("Gill Sans", 8, 'bold'))
    title1.place(x=10, y=50)
    intro1 = Message(about, width=650, bg='#6FE2FA', text="Cette application a été conçue dans le cadre du projet de fin d'études pour l'obtention d'un master en informatique. Le travail de cette application est d'utiliser des algorithmes d'apprentissage automatique et de les appliquer à un ensemble de données pour arriver à un modèle spécifique, sur la base duquel nous pouvons prédire si nous avons un nouveau cas.")
    intro1.place(x=50, y=70)

    isolateur = Frame(win, bg='#6FE2FA', height=500, width=800)
    isolateur.place(x=0, y=0)
    # Home

    home = Frame(win, bg='#0994AD', height=500, width=800)
    home.place(x=0, y=0)
    # title
    title = Label(home, bg='#0994AD', text="Saisir les données du patient à examiner", fg='white', font=("Gill Sans", 15, 'bold'))
    title.place(x=210, y=80)

    intro = Message(home, bg='#0994AD', justify=CENTER, width=550, font=("Gill Sans", 9, 'bold'), fg='white', text="Cette application a utilisé les techniques d'apprentissage autaomatique pour détecter les maladies cardiovasculaires comme les crises cardiaques, les maladies coronariennes")
    intro.place(x=150, y=20)
    # Form
    forme = Frame(home, bg='#a3f8f0', height=390, width=800)
    forme.place(x=0, y=110)

    # labels information_____________________________________

    label1 = Label(home, text=' Age', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#382861').place(x=30, y=135)
    text1 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text1.place(x=175, y=135)
    texts.append(text1)

    label2 = Label(home, text=' Sexe', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#382861').place(x=30, y=170)
    text2 = ttk.Combobox(home, values=["Homme", "Femme"], font=("Gill Sans", 15), width=14)
    home.option_add('*TCombobox*Listbox.foreground' % home, '#460303')
    text2.config(foreground="#382861")
    text2.current(0)
    text2.place(x=175, y=170)
    texts.append(text2)

    label3 = Label(home, text=' Douleur thoracique ', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#382861').place(x=30, y=205)
    cp = ["Angine typique", "Angine atypique", "Douleur non angineuse", "Asymptomatique"]
    text3 = ttk.Combobox(home, values=cp, font=("Gill Sans", 15), width=14)
    text3.current(3)
    text3.place(x=175, y=205)
    text3.config(foreground="#382861")
    texts.append(text3)

    label4 = Label(home, text=' Tension artérielle', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=30, y=240)
    text4 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text4.place(x=175, y=240)
    texts.append(text4)

    label5 = Label(home, text=' Cholestérol', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=30, y=275)
    text5 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text5.place(x=175, y=275)
    texts.append(text5)

    label6 = Label(home, text=' Glycémie à jeun ', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=30, y=310)
    text6 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text6.place(x=175, y=310)
    texts.append(text6)

    label7 = Label(home, text=' ECG', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=30, y=345)
    text7 = ttk.Combobox(home, values=["Normal", "Anomalie de ST-T", "Hypertrophie ventriculaire gauche"], font=("Gill Sans", 15), width=14)
    text7.current(0)
    text7.place(x=175, y=345)
    text7.config(foreground="#382861")
    texts.append(text7)

    label8 = Label(home, text='Fréquence cardiaque max', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=135)
    text8 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text8.place(x=575, y=135)
    texts.append(text8)

    label9 = Label(home, text="Angine par l'effort", font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=170)
    text9 = ttk.Combobox(home, values=["Oui", "Non"], font=("Gill Sans", 15), width=14)
    text9.current(1)
    text9.place(x=575, y=170)
    text9.config(foreground="#382861")
    texts.append(text9)

    label10 = Label(home, text='Dépression ST ', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=205)
    text10 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text10.place(x=575, y=205)
    texts.append(text10)

    label11 = Label(home, text=' Pente du segment ST ', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=240)
    text11 = ttk.Combobox(home, values=["Montant", "Plat", "Descendant"], font=("Gill Sans", 15), width=14)
    text11.current(1)
    text11.place(x=575, y=240)
    text11.config(foreground="#382861")
    texts.append(text11)

    label12 = Label(home, text='Nb de gros vaisseaux', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=275)
    text12 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text12.place(x=575, y=275)
    texts.append(text12)

    label13 = Label(home, text='Thalassémie ', font=("Gill Sans", 10, 'bold'), bg='#a3f8f0', fg='#49357a').place(x=400, y=310)
    text13 = Entry(home, bg='white', font=("Gill Sans", 15), width=16, fg='#460303')
    text13.place(x=575, y=310)
    texts.append(text13)

    # Button___________________________________

    check_button = Button(home, text=' Prédire ', font=("Gill Sans", 12, 'bold'), bg='#2f5376', fg='white', cursor="hand2", borderwidth='4', relief=RAISED, command=check_empty)
    check_button.place(x=500, y=418)
    cancel_button = Button(home, text=' Annulé ', font=("Gill Sans", 12, 'bold'), bg='#5a738c', fg='white', cursor="hand2", borderwidth='4', relief=RAISED, command=clear_text)
    cancel_button.place(x=590, y=418)
    # Calling Main()

    win.mainloop()


if __name__ == '__main__':
    main()
