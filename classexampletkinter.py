from tkinter import *



def main():
    root = Tk()
    window1= window(root, "Class based windows", '400x400', 'Ramlethal Valentine')

class window:
    n = 0


    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry) #input 'sizexsize'
        Label(self.root, text=message).pack()
        button1 = Button(self.root, text='Increment', command=self.Increment)
        button1.pack()
        self.root.mainloop()

    def Increment(self):
        self.n += 1
        print(self.n)
        return None

main()
