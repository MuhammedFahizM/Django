import tkinter as tk
from tkinter import messagebox

# Create the main window

root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")

# Function to handle login

def login():
    username = username_entry.get()
    password = password_entry.get()

    #Simple login check(you can replace this with real logic)
    if username == "Fahiz" and password == "1234":
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed",f"Invalid username or password!")

heading = tk.Label(root,text="Login",font=("Ariel",16,"bold"))
heading.pack(pady=10)


#Username label and entry
username_label = tk.Label(root,text="Username:",font=("Areil",13,"bold"))
heading.pack()
username_entry = tk.Entry(root,font=("Ariel",13))
username_entry.pack()

# Password label and entry
password_label = tk.Label(root,text="Password",font=("Ariel",12))
password_label.pack()
password_entry = tk.Entry(root,font=("Ariel",12),show="*")
password_entry.pack()

#Login button
login_button = tk.Button(root,text="Login",font=("Ariel",12,"bold"),command=login)
login_button.pack(pady=10)

root.mainloop()