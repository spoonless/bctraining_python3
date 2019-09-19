'''
Created on 16 sept. 2019

@author: david
'''
import sys

MOYENNE = 1.70


def saisir_nombre(question, error_msg="Ce n'est pas un nombre !"):
    while True:
        try:
            return float(input(f"{question} "))
        except ValueError:
            print(error_msg, file=sys.stderr)


taille = saisir_nombre(question="Quelle est votre taille ?",
                       error_msg="Vous devez saisir un nombre !")
ecart_moyenne = taille - MOYENNE
print(f"Vous avez un écart de {ecart_moyenne:.2f} par rapport à la moyenne.")
