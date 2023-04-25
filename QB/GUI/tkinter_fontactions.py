import tkinter as tk
parent = tk.Tk()
parent.title("FONT")
label = tk.Label(parent,text = "Welcome to Python tkinter Basic exercises-", font =("Bold",10))
label.grid(column=0,row=0)
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 70))
my_label.grid(column=0, row=10)
parent.mainloop()
