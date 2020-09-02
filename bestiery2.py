from tkinter import *
from PIL import ImageTk, Image
import psycopg2

try:
    #Connect to an existing database

    conn = psycopg2.connect(host='localhost', port=5433, dbname='postgres', user='postgres', password='slugger123')
    print('Connection Established')

    cur = conn.cursor()

    cur.execute("""
    DROP TABLE IF EXISTS Besitary_of_Demons;
    CREATE TABLE Besitary_of_Demons
    (
    id SERIAL,
    Demon TEXT NOT NULL,
    Race TEXT NOT NULL,
    Year_of_Debut INTEGER,
    Sex TEXT NOT NULL,
    Skills TEXT NOT NULL,
    Backstory TEXT NOT NULL
    )
    """)


    #Commit the change
    conn.commit()

except:
    print("The Connection with the Database is not established")
    quit()

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


image1 = Button(frame1, image=demifiend1)
image1.grid(column=0, row=0)

image2 = Button(frame2, image=Alice)
image2.grid(column=1, row=0)







#Close the connection
conn.close()









root.mainloop()
