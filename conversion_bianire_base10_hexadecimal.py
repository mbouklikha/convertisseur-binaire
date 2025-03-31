#Programme réalisé par BOUKLIKHA Mohamed-Amine => PC : 22
from tkinter import *

#Base de la fenetre
fenetre = Tk()
fenetre.title("Projet 3")
fenetre.config(width=500, height=268, bg='#F0FFF0')

#Texte pour indiquer le convertisseur du haut qui permet de convertir du binaire en decimal et en hexadecimal
BaseH2 = Label(fenetre, text='En base 2 :', bg='#BDB76B', fg='black', font=('arial', 10, 'bold'))
BaseH2.place(x=0, y=70)
BaseH10 = Label(fenetre, text='En base 10 :', bg='#BDB76B', fg='black', font=('arial', 10, 'bold'))
BaseH10.place(x=0, y=90)
BaseH16 = Label(fenetre, text='En base 16 :', bg='#BDB76B', fg='black', font=('arial', 10, 'bold'))
BaseH16.place(x=0, y=110)

#Texte pour indiquer le convertisseur en bas qui permet de convertir le decimal en binaire et en hexadecimal
BaseB10 = Label(fenetre, text='En base 10 :', bg='#1E90FF', fg='black', font=('arial', 10, 'bold'))
BaseB10.place(x=0, y=200)
BaseB2 = Label(fenetre, text='En base 2 :', bg='#1E90FF', fg='black', font=('arial', 10, 'bold'))
BaseB2.place(x=0, y=220)
BaseB16 = Label(fenetre, text='En base 16 :', bg='#1E90FF', fg='black', font=('arial', 10, 'bold'))
BaseB16.place(x=0, y=240)

#Création des boutons en haut à gauche pour ecrire en binaire
def ButtonH1():
    if BoutonH1.cget("text") == str(0):
        BoutonH1.config(text="1",fg='red')
    elif BoutonH1.cget("text") == str(1):
        BoutonH1.config(text="0",fg='black')

BoutonH1 = Button(fenetre, text="0", command=ButtonH1)
BoutonH1.place(x=20, y=20)

def ButtonH2():
    if BoutonH2.cget("text") == str(0):
        BoutonH2.config(text="1",fg='red')
    elif BoutonH2.cget("text") == str(1):
        BoutonH2.config(text="0",fg='black')

BoutonH2 = Button(fenetre, text="0", command=ButtonH2)
BoutonH2.place(x=60, y=20)

def ButtonH3():
    if BoutonH3.cget("text") == str(0):
        BoutonH3.config(text="1",fg='red')
    elif BoutonH3.cget("text") == str(1):
        BoutonH3.config(text="0",fg='black')

BoutonH3 = Button(fenetre, text="0", command=ButtonH3)
BoutonH3.place(x=100, y=20)

def ButtonH4():
    if BoutonH4.cget("text") == str(0):
        BoutonH4.config(text="1",fg='red')
    elif BoutonH4.cget("text") == str(1):
        BoutonH4.config(text="0",fg='black')

BoutonH4 = Button(fenetre, text="0", command=ButtonH4)
BoutonH4.place(x=140, y=20)

def ButtonH5():
    if BoutonH5.cget("text") == str(0):
        BoutonH5.config(text="1",fg='red')
    elif BoutonH5.cget("text") == str(1):
        BoutonH5.config(text="0",fg='black')

BoutonH5 = Button(fenetre, text="0", command=ButtonH5)
BoutonH5.place(x=180, y=20)

def ButtonH6():
    if BoutonH6.cget("text") == str(0):
        BoutonH6.config(text="1",fg='red')
    elif BoutonH6.cget("text") == str(1):
        BoutonH6.config(text="0",fg='black')

BoutonH6 = Button(fenetre, text="0", command=ButtonH6)
BoutonH6.place(x=220, y=20)

def ButtonH7():
    if BoutonH7.cget("text") == str(0):
        BoutonH7.config(text="1",fg='red')
    elif BoutonH7.cget("text") == str(1):
        BoutonH7.config(text="0",fg='black')

BoutonH7 = Button(fenetre, text="0", command=ButtonH7)
BoutonH7.place(x=260, y=20)

def ButtonH8():
    if BoutonH8.cget("text") == str(0):
        BoutonH8.config(text="1",fg='red')
    elif BoutonH8.cget("text") == str(1):
        BoutonH8.config(text="0",fg='black')

BoutonH8 = Button(fenetre, text="0", command=ButtonH8)
BoutonH8.place(x=300, y=20)

#Création des boutons en bas à gauche pour ecrire en decimal

def ButtonB1():
    if BoutonB1.cget("text") == str(0):
        BoutonB1.config(text="1")
    elif BoutonB1.cget("text") == str(1):
        BoutonB1.config(text="2")
    elif BoutonB1.cget("text") == str(2):
        BoutonB1.config(text="3")
    elif BoutonB1.cget("text") == str(3):
        BoutonB1.config(text="4")
    elif BoutonB1.cget("text") == str(4):
        BoutonB1.config(text="5")
    elif BoutonB1.cget("text") == str(5):
        BoutonB1.config(text="6")
    elif BoutonB1.cget("text") == str(6):
        BoutonB1.config(text="7")
    elif BoutonB1.cget("text") == str(7):
        BoutonB1.config(text="8")
    elif BoutonB1.cget("text") == str(8):
        BoutonB1.config(text="9")
    elif BoutonB1.cget("text") == str(9):
        BoutonB1.config(text="0")

BoutonB1 = Button(fenetre, text="0", command=ButtonB1)
BoutonB1.place(x=20, y=150)

def ButtonB2():
    if BoutonB2.cget("text") == str(0):
        BoutonB2.config(text="1")
    elif BoutonB2.cget("text") == str(1):
        BoutonB2.config(text="2")
    elif BoutonB2.cget("text") == str(2):
        BoutonB2.config(text="3")
    elif BoutonB2.cget("text") == str(3):
        BoutonB2.config(text="4")
    elif BoutonB2.cget("text") == str(4):
        BoutonB2.config(text="5")
    elif BoutonB2.cget("text") == str(5):
        BoutonB2.config(text="6")
    elif BoutonB2.cget("text") == str(6):
        BoutonB2.config(text="7")
    elif BoutonB2.cget("text") == str(7):
        BoutonB2.config(text="8")
    elif BoutonB2.cget("text") == str(8):
        BoutonB2.config(text="9")
    elif BoutonB2.cget("text") == str(9):
        BoutonB2.config(text="0")

BoutonB2 = Button(fenetre, text="0", command=ButtonB2)
BoutonB2.place(x=60, y=150)

def ButtonB3():
    if BoutonB3.cget("text") == str(0):
        BoutonB3.config(text="1")
    elif BoutonB3.cget("text") == str(1):
        BoutonB3.config(text="2")
    elif BoutonB3.cget("text") == str(2):
        BoutonB3.config(text="3")
    elif BoutonB3.cget("text") == str(3):
        BoutonB3.config(text="4")
    elif BoutonB3.cget("text") == str(4):
        BoutonB3.config(text="5")
    elif BoutonB3.cget("text") == str(5):
        BoutonB3.config(text="6")
    elif BoutonB3.cget("text") == str(6):
        BoutonB3.config(text="7")
    elif BoutonB3.cget("text") == str(7):
        BoutonB3.config(text="8")
    elif BoutonB3.cget("text") == str(8):
        BoutonB3.config(text="9")
    elif BoutonB3.cget("text") == str(9):
        BoutonB3.config(text="0")

BoutonB3 = Button(fenetre, text="0", command=ButtonB3)
BoutonB3.place(x=100, y=150)


#Création du boutons pour convertir le haut ( binaire en decimal et en hexadecimal )
def Conversion1():
    H1 = BoutonH1.cget('text')
    H2 = BoutonH2.cget('text')
    H3 = BoutonH3.cget('text')
    H4 = BoutonH4.cget('text')
    H5 = BoutonH5.cget('text')
    H6 = BoutonH6.cget('text')
    H7 = BoutonH7.cget('text')
    H8 = BoutonH8.cget('text')
    nb = str(H1)+str(H2)+str(H3)+str(H4)+str(H5)+str(H6)+str(H7)+str(H8)
    BaseH2.config(text="En base 2 : " +nb)
    nd = 0
    for bit in nb:
        nd = nd * 2 + int(bit)
    BaseH10.config(text='En base 10 : ' + str(nd))
    nh = (int(nd) // 16 ** 2, int(nd) // 16, int(nd) % 16)
    BaseH16.config(text='En base 16 : ' + str(nh))

ConversionH1 = Button(fenetre, text="B > D et H", command=Conversion1)
ConversionH1.place(x=400, y=20)

#Création du boutons pour convertir le bas ( decimal en binaire et en hexadecimal )
def Conversion2():
    B1 = BoutonB1.cget('text')
    B2 = BoutonB2.cget('text')
    B3 = BoutonB3.cget('text')
    dc = str(B1)+str(B2)+str(B3)
    BaseB10.config(text="En base 10 : " + dc)
    binaire = ''
    while dc != 0:
        binaire = str(int(dc) % 2) + binaire
        dc = int(dc) // 2
    BaseB2.config(text="En base 2 : " + str(binaire))
    nbh = (int(dc) // 16 ** 2, int(dc) // 16, int(dc) % 16)
    BaseB16.config(text="En base 16 : " + str(nbh))

ConversionB1 = Button(fenetre, text="D > B et H", command=Conversion2)
ConversionB1.place(x=400, y=150)

fenetre.mainloop()