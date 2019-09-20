'''
Created on 20 sept. 2019

@author: david
'''
import tkinter as tk
import tkinter.messagebox as messagebox

window = tk.Tk()

nom = tk.StringVar()
age = tk.IntVar()

def valider():
    messagebox.showinfo("Bonjour", f"Bonjour {nom.get()} ! Tu as {age.get()} ans.")

libelle = tk.Label(window, text="Nom")
libelle.grid(column=0, row=0)

libelle = tk.Label(window, text="Age")
libelle.grid(column=0, row=1)

entry = tk.Entry(window, textvariable=nom)
entry.grid(column=1, row=0)

entry = tk.Entry(window, textvariable=age)
entry.grid(column=1, row=1)

bouton = tk.Button(window, text="Ok", command=valider)
bouton.place(anchor=tk.CENTER)
bouton.grid(column=0, row=2, padx=5, pady=5)

bouton = tk.Button(window, text="Cancel", command=window.destroy)
bouton.place(anchor=tk.CENTER)
bouton.grid(column=1, row=2)

window.mainloop()
