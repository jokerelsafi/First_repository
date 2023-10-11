utf-8

import tkinter
from tkinter import messagebox

app = tkinter.Tk()
app.geometry("400x400")
app.title("gui tkinter")

def confirmer():
    messagebox.showerror("ERREUR", "une erreur est survenue")

var_label = tkinter.StringVar()
var_entry = tkinter.StringVar()

def update_label(*args):
    var_label.set(var_entry.get())

var_entry.trace("w", update_label)

entry = tkinter.Entry(app, show ="*", textvariable=var_entry)
label = tkinter.Label(app, text = "wecome", textvariable= var_label)
radio1 = tkinter.Radiobutton(app, text = "Homme", value = 1)
radio2 = tkinter.Radiobutton(app, text = "femme", value = 2)
button = tkinter.Button(app, text = "confirmer", command = confirmer)
listbox = tkinter.listbox(app)
listbox.insert(1, "windows")
listbox.insert(2, "MacOS")
listbox.insert(3, "Linux")

entry.pack()
label.pack()
radio1.pack()
radio2.pack()
button.pack()
listbox.pack()

app.mainloop()
