import tkinter as tk
from tkinter import LabelFrame, Button, Label, Toplevel
from PIL import ImageTk, Image
import psycopg2

root = tk.Tk()

try:
    #connect to an existing database

    conn = psycopg2.connect(host='localhost', port=5433, dbname='postgres', user='postgres', password='slugger123')
    print('Connection established')
    cur = conn.cursor()

except:
    print("The Connection with the Database is not established")
    quit()


class FrontpageBestiery:
    #For ease to add buttons

    def __init__(self, root, img_filename, column, row, Name):
        self.root = root
        self.root.title('Class test')

        self.image = ImageTk.PhotoImage(Image.open(img_filename).resize((200,200), Image.ANTIALIAS))
        self.framename = Name

        self.frame = LabelFrame(self.root, text=self.framename)
        self.frame.grid(row=row, column=column)

        self.button = Button(self.frame, image=self.image, command=self.clicker)
        self.button.grid(column=column, row=row)


    #Write a function that gathers info on the demons from the database

    def clicker(self):
        top = Toplevel()
        top.title(self.framename)

        monsterframe = LabelFrame(top)
        monsterframe.grid(column=0, row=0, rowspan=50)
        Raceframe = LabelFrame(top, text='Race')
        Raceframe.grid(column=3, row=0)
        Typeframe = LabelFrame(top, text='Type')
        Typeframe.grid(column=3, row=1)
        Sexframe = LabelFrame(top, text='Sex')
        Sexframe.grid(column=3, row=2)
        backframe = LabelFrame(top, text='Background')
        backframe.grid(column=3, row=3)
        Alignmentframe = LabelFrame(top, text='Alignment')
        Alignmentframe.grid(column=3, row=4)


        #Gather your information

        cur.execute("SELECT * FROM besitary_of_demons WHERE Name = %s ", [self.framename])
        backg = cur.fetchall()

        for backg in backg:
            backg = backg

        #Gui for the demon info

        Label(monsterframe, image=self.image).pack()
        Label(Raceframe, text=backg[2]).pack()
        Label(Typeframe, text=backg[5]).pack()
        Label(Sexframe, text=backg[4]).pack()
        Label(backframe, text=backg[6], wraplength=300).pack()
        Label(Alignmentframe, text=backg[7]).pack()






Demifiend = FrontpageBestiery(root, r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png",0,0, 'Demifiend')

Alice = FrontpageBestiery(root, r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Alice.jpg",1,0, 'Alice')

Chernobog = FrontpageBestiery(root, r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Chernobog.png",2,0, 'Chernobog')

Kogo_Saburo = FrontpageBestiery(root, r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Koga-Saburo.jpg",3,0, 'Koga Saburo')

root.mainloop()
