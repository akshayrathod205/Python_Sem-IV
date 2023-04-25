import tkinter as tk

def write_text():
    lbl = tk.Label(parent)
    lbl.config(text = "Greetings User")
    lbl.place(x=160,y=90)
    print("Tkinter is easy to create GUI!")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp= tk.Button(frame,text="Hello",command=write_text)
text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,text="Exit",fg="green",command=parent.destroy)
exit_button.pack(side=tk.RIGHT)

parent.geometry("400x400")
parent.mainloop()