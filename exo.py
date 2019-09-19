'''
Created on 16 sept. 2019

@author: david
'''

def mon_divmod(numerateur, denominateur):
    resultat = numerateur // denominateur
    reste = numerateur % denominateur
    return resultat, reste

def calcul_prix_ttc(prix_ht, taux_tva = 20):
    # déclaration de la variable tva
    tva = prix_ht * taux_tva / 100
    tva = round(tva, 2)
    return prix_ht + tva