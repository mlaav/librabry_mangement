from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import psycopg2
def bookRegister():
    bid=bookInfo1.get()
    title=bookInfo2.get()
    author=bookInfo3.get()
    status=status.lower()
    insertBooks="insert into"+booktable+"values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cursor.execute(insertBooks)
        conn.commit()
        messagebox.showinfo('succes',"Book added successfully")
    except:
        messagebox.showinfo("Error","can't add data into database")
    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()