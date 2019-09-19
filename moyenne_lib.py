'''
Created on 17 sept. 2019

@author: david
'''

def moyenne(x, *args):
    """Calcule la moyenne d'un nombre quelconque de valeurs passées en paramètres."""
    nb = 1 + len(args)
    somme = x + sum(args)
    return somme / nb
