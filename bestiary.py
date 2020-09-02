from tkinter import *
from PIL import ImageTk, Image

def demifiend_open():
    global demifiend
    demitop = Toplevel()
    demitop.title('Demifiend')
    demifiend = ImageTk.PhotoImage(Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png"))
    DemiFrame = Label(demitop, image=demifiend)
    DemiFrame.grid(column=0, row=0)
    frame1 = LabelFrame(demitop, text='Backstory')
    frame1.grid(column=1, row=0)
    Backstory = Label(frame1, text="To allow the protagonist to survive in a now demon-ridden world, the nursemaid subdues him and the child drops a Magatama — the essence of demonic power — into the protagonist's eye; allowing the parasite entity to merge with him, resulting in the birth of the Demi-fiend — a being with the body of a demon and the heart of a human.The protagonist's body has now been altered, with glowing tattoos emerging on his skin and a horn that grew from his nape as proof of ingesting the Magatama. He now has an incredible destiny on his shoulders: He is to either create the new world by supporting a Reason, deviate from the process to return the world to its prior state, or completely shed his humanity by embracing his demonic self and put an end the process of the world's destruction and rebirth.", wraplength=500, justify=LEFT)
    Backstory.grid(column=1, row=0)
    frame2 = LabelFrame(demitop, text='Power Level')
    frame2.grid(column=1, row=1)
    Power_Lvl = Label(frame2, text='Overall Strength Rank: A')
    Power_Lvl.grid(column=1, row=0)

root = Tk()

root.title('Besitary for Shin Megami Tensei')
root.geometry('800x800')

frame1 = LabelFrame(root, text='Demi Fiend')
frame1.grid(column=0, row=0)
frame2 = LabelFrame(root, text='Alice')
frame2.grid(column=1, row=0)

demifiend = Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Demi-Fiend1.png")
demifiendresize =demifiend.resize((200, 200), Image.ANTIALIAS)
demifiend1 = ImageTk.PhotoImage(demifiendresize)
Alice = Image.open(r"S:\Projects\Python Projects\Python Review\tkinter training\New folder\Alice.jpg")
Alice = Alice.resize((200, 200), Image.ANTIALIAS)
Alice = ImageTk.PhotoImage(Alice)


image1 = Button(frame1, image=demifiend1, command=demifiend_open)
image1.grid(column=0, row=1)

image2 = Button(frame2, image=Alice, command=open)
image2.pack()
 




root.mainloop()
