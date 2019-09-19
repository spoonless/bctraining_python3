'''
Created on 16 sept. 2019

@author: david
'''
MOYENNE = 1.70

taille_saisie = input("Quelle est votre taille ? ")
taille = float(taille_saisie)
ecart_moyenne = taille - MOYENNE
print(f"Vous avez un écart de {ecart_moyenne:.2f} par rapport à la moyenne.")
