'''
Created on 17 sept. 2019

@author: david
'''

def demander_valeurs():
    valeurs=[]
    
    for i in range(10):
        valeurs.append(float(input("Une valeur : ")))

    return valeurs

valeurs = demander_valeurs()

somme = 0
for v in valeurs:
    somme += v

moyenne = somme / len(valeurs)
print(f"Moyenne : {moyenne:.3f}")
