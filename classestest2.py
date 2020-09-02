import tkinter as tk
from tkinter import LabelFrame
from tkinter import Button
from PIL import ImageTk, Image
import psycopg2

root = tk.Tk()
root.title('ClassTkTest')
root.geometry('400x400')

class frontpagebestiery:

    photo = ImageTk.PhotoImage(Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png"))

    def __init__(self, main, photo, column, row):
        self.firstframe = LabelFrame(main)
        self.firstframe.grid(column=0,row=0)

        self.demon = Button(main, image=photo)
        self.demon.grid(column=column, row=row)

demon = frontpagebestiery(root, r"S:/Projects/Python Projects/Python Review/tkinter training/New folder/Demi-Fiend1.png", 1,1)

root.mainloop()
