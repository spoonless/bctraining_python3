'''
Created on 20 sept. 2019

@author: david
'''
import tkinter as tk

window = tk.Tk()

message = tk.StringVar()

compteur = 0

def dire_bonjour():
    global compteur
    message.set(f"Bonjour {compteur}")
    compteur += 1
    
libelle = tk.Label(window, textvariable=message)
libelle.grid(column=1, row=0)

bouton = tk.Button(window, text="Ok", command=dire_bonjour)
bouton.grid(column=0, row=0)

window.mainloop()
