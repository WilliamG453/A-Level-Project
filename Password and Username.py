import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
#Properties for the window/canvas
window = Tk()
window.title("Login Screen")
window.geometry("200x200")

#Creating the login screen
lbl = Label(window, text="Please Login to Continue", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

#Username and Password
Username = ("Will")
Password = ("Will")

def clicked():
    print("Trying to login...")
    if UsernameText.get() == Username and PasswordText.get() == Password:
        messagebox.showinfo("Success", "You are now Logged in!")
    else:
        messagebox.showerror("Warning","Username or Password is Incorrect")

#Login Button
btn = Button(window, text="Login", bg="black", fg="white", command=clicked)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)
#Username
lbl = Label(window, text = "Username", font=("Arial Bold", 10))
lbl.place(relx=0.18, rely=0.35, anchor=CENTER)
UsernameText = txt = Entry(window,width=10)
txt.place(relx=0.5, rely=0.35, anchor=CENTER)
#Password
lbl = Label(window, text = "Password", font=("Arial Bold", 10))
lbl.place(relx=.17, rely=0.5, anchor=CENTER)
PasswordText = txt = Entry(window,width=10, show="*")
txt.place(relx=.5, rely=0.5, anchor=CENTER)


window.mainloop()
