import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

 # Adding a label
 
label = tk.Label(root,text="Hello, Tkinter",font=("Ariel",16))
label.pack()  # Places it on window

#Adding a button
button = tk.Button(root,text="Click me!",font=("Ariel",12),command=lambda:print("Button clicked!"))
button.pack()
root.geometry("400x300")
root.mainloop()
