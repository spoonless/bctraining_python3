'''
Created on 18 sept. 2019

@author: david
'''
from voiture import BoiteDeVitesse


b = BoiteDeVitesse(rapports=5)

b.monter_rapport()
b.monter_rapport(2)
b.monter_rapport(232)

print(b.rapport_courant)

while not b.au_point_mort:
    b.retrograder()

b.passer_marche_arriere()
print(b.rapport_courant)
