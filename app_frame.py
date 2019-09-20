'''
Application graphique simple. Exemple de l'utilisation de la programmation
objet pour créer une classe spécialisée de Frame.

@author: David Gayerie
'''
import tkinter as tk

class InfoContactFrame(tk.Frame):
    
    def __init__(self, root, **kwargs):
        super().__init__(root)
        self.pack()
        self.champs = {
            "nom": tk.StringVar(),
            "prénom": tk.StringVar(),
            "adresse": tk.StringVar(),
            "code postal": tk.StringVar(),
            "ville": tk.StringVar(),
        }
        
        for k, v in kwargs.items():
            if k in self.champs:
                self.champs[k].set(v)

        for ligne, (libelle, var) in enumerate(self.champs.items()):
            label = tk.Label(self, text=libelle.capitalize())
            label.grid(sticky=tk.E, row=ligne, column=0)
            entry = tk.Entry(self, textvariable=var)
            entry.grid(sticky=tk.W, row=ligne, column=1, columnspan=2)

        btn = tk.Button(self, text="ok", command=lambda:self._printConsole())
        btn.grid(sticky=tk.E, row=len(self.champs), column=2)

    def _printConsole(self):
        for k, v in self.champs.items():
            print(f"{k} = {v.get()}")


window = tk.Tk()
window.title("Info Contact")
app = InfoContactFrame(window, ville="Niort")
app.mainloop()
