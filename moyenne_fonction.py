'''
Created on 16 sept. 2019

@author: david
'''
MOYENNE = 170


def demander_taille():
    """Cette fonction demande sa taille à l’utilisateur et retourne la valeur 
       saisie sous la forme d’un nombre."""
    taille_saisie = input("Quelle est votre taille ? ")
    return float(taille_saisie) * 100


def comparer_taille(taille1, taille2=MOYENNE):
    return taille1 - taille2


def afficher_difference_moyenne(difference_moyenne):
    print(f"Vous avez un écart de {difference_moyenne:.0f} cm par rapport à la moyenne qui est de {MOYENNE} cm.")

if __name__ == "__main__":
    taille = demander_taille()
    difference = comparer_taille(taille)
    afficher_difference_moyenne(difference)
