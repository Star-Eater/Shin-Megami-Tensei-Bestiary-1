import tkinter as tk
from tkinter import LabelFrame
from tkinter import Button
from tkinter import Toplevel
from tkinter import Label
from PIL import ImageTk, Image
import psycopg2

root = tk.Tk()
root.title('ClassTkTest')
root.geometry('400x400')

class frontpagebestiery:

    def __init__(self, main):
        self.firstframe = LabelFrame(main)
        self.firstframe.pack()
        self.demifiend = Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png")
        self.demifiendresize =self.demifiend.resize((200, 200), Image.ANTIALIAS)
        self.demifiend1 = ImageTk.PhotoImage(self.demifiendresize)
        image1 = Button(self.firstframe, image=self.demifiend1, command=self.demiclick)
        image1.grid(column=0, row=1)

    def demiclick(self):
        self.demitop = Toplevel()
        self.demitop.title('Demifiend')
        self.demifiend = ImageTk.PhotoImage(Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png"))
        self.DemiFrame = Label(self.demitop, image=self.demifiend)
        self.DemiFrame.grid(column=0, row=0)
        self.frame1 = LabelFrame(self.demitop, text='Backstory')
        self.frame1.grid(column=1, row=0)
        self.Backstory = Label(self.frame1, text="To allow the protagonist to survive in a now demon-ridden world, the nursemaid subdues him and the child drops a Magatama — the essence of demonic power — into the protagonist's eye; allowing the parasite entity to merge with him, resulting in the birth of the Demi-fiend — a being with the body of a demon and the heart of a human.The protagonist's body has now been altered, with glowing tattoos emerging on his skin and a horn that grew from his nape as proof of ingesting the Magatama. He now has an incredible destiny on his shoulders: He is to either create the new world by supporting a Reason, deviate from the process to return the world to its prior state, or completely shed his humanity by embracing his demonic self and put an end the process of the world's destruction and rebirth.", wraplength=500, justify=LEFT)
        self.Backstory.grid(column=1, row=0)
        self.frame2 = LabelFrame(self.demitop, text='Power Level')
        self.frame2.grid(column=1, row=1)
        self.Power_Lvl = Label(self.frame2, text='Overall Strength Rank: A')
        self.Power_Lvl.grid(column=1, row=0)


Demon = frontpagebestiery(root)


root.mainloop()
