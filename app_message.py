"""
Exemple simple d'application pour afficher un message saisi dans une boite
de dialogue.

@author: David Gayerie
"""
import tkinter as tk
import tkinter.messagebox as mb

app = tk.Tk()

libelle = tk.Label(app, text="Message : ")
libelle.grid(column=0, row=0)

zone_saisie = tk.Entry(app)
zone_saisie.grid(column=1, row=0)

def button_clique():
    mb.showinfo("Message info", zone_saisie.get())

boutton = tk.Button(app, text="Valider", command=button_clique)
boutton.grid(column=0, row=1)

boutton_quitter = tk.Button(app, text="Quitter", command=lambda: app.quit())
boutton_quitter.grid(column=1, row=1)

app.mainloop()