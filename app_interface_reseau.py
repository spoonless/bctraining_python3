"""
Exemple d'une interface graphique pour simuler une interaction avec une
interface réseau.

@author: David Gayerie
"""
import tkinter as tk
import tkinter.ttk as ttk

def app_interface_reseau(func):
    def boutton_clique():
        func(interface_reseau.get(), vitesse_transfert.get(), mode_synchrone.get())
        
    app = tk.Tk()
    app.title("Lanceur")
    
    interface_reseau = tk.StringVar()
    vitesse_transfert = tk.IntVar()
    vitesse_transfert.set(300)
    mode_synchrone = tk.BooleanVar()
    mode_synchrone.set(True)
    
    libelle = tk.Label(app, text="Interface réseau")
    libelle.grid(column=0, row=0)
    zone_saisie = tk.Entry(app, textvariable=interface_reseau)
    zone_saisie.grid(column=1, row=0)
    
    rd = ttk.Radiobutton(app, text="300mb/s", value=300, variable=vitesse_transfert)
    rd.grid(column=0, row=1)
    rd = ttk.Radiobutton(app, text="600mb/s", value=600, variable=vitesse_transfert)
    rd.grid(column=1, row=1)
    rd = ttk.Radiobutton(app, text="1000mb/s", value=1000, variable=vitesse_transfert)
    rd.grid(column=2, row=1)
    
    cb = ttk.Checkbutton(app, text="Mode synchrone", variable=mode_synchrone)
    cb.grid(column=0, row=2)
    
    boutton = tk.Button(app, text="Afficher", command=boutton_clique)
    boutton.grid(column=0, row=3)
    
    app.mainloop()

def afficher_choix_utilisateur(interface_reseau, vitesse_transfert, mode_synchrone):
    print(f"Interface réseau : {interface_reseau}")
    print(f"Vitesse de transfert : {vitesse_transfert}")
    print(f"Mode synchrone : {mode_synchrone}")

app_interface_reseau(afficher_choix_utilisateur)
