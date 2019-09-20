'''
Application simple pour donner un exemple de widgets de TkInter.

@author: David Gayerie
'''
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as mb

window = tk.Tk()
window.title("My GUI")

label = tk.Label(window, text="Hello", font=font.Font(size= 24, weight= "bold"))
label.grid(column=0, row=0)

value = tk.StringVar()

text = tk.Entry(window, width=10, textvariable=value)
text.grid(column=1, row=0)
text.focus()

def clicked():
    mb.showinfo("Message", f"Message de l'utilisateur : {value.get()}")

combo = ttk.Combobox(window, text="choix", values=(1, 2, 3))
combo.grid(column=0, row=1)
combo.current(1)

button = tk.Button(window, text="Click me", command=clicked)
button.grid(column=2, row=0)

opinion = tk.IntVar()
for i, rb_label in enumerate(["oui", "non", "peut-être"]):
    rb = ttk.Radiobutton(window, text=rb_label, value=i, variable=opinion)
    rb.grid(column=i, row=3)


window.mainloop()