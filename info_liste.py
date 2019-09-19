'''
Created on 17 sept. 2019

@author: david
'''

liste_valeurs = []

while True:
    valeur = input("Une valeur : ")
    if valeur == '':
        break
    
    liste_valeurs.append(float(valeur))

if not liste_valeurs:
    print("Vous n'avez saisi aucun nombre.")
elif len(liste_valeurs) == 1:
    print(f"Vous n'avez que {liste_valeurs[0]:10.2f}")
else:
    min_valeur = min(liste_valeurs)
    max_valeur = max(liste_valeurs)
    somme_valeurs = sum(liste_valeurs)
    moyenne_valeurs = somme_valeurs / len(liste_valeurs)
    
    print(f"Min :     {min_valeur:10.2f}")
    print(f"Max :     {max_valeur:10.2f}")
    print(f"Somme :   {somme_valeurs:10.2f}")
    print(f"Moyenne : {moyenne_valeurs:10.2f}")
