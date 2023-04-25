import tkinter as tk
root=tk.Tk()
root.title("Text widhget")
mytext=tk.Text(root)
mytext.insert('1.0',"Python excercise")
mytext.insert('1.20','Practicing')

def remove():
    mytext.delete('1.0')
    mytext.delete('end - 2 chars')
    
btn = tk.Button(root, text='Click', command=remove)
btn.place(x=50, y=50)

mytext.pack()

root.mainloop()
