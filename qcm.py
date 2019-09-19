'''
Created on 16 sept. 2019

@author: david
'''

score = 0

print("Quel est le meilleur langage de programmation ?")
reponse = input()
score += int(reponse == "Python")

print("Quelle est l'extension d'un fichier Python ?")
reponse = input()
score += int(reponse == ".py")

print("Avez-vous des questions ?")
reponse = input()
score += int(reponse == "non")

print(f"Réponses correctes : {score}")
print(f"Réponses incorrectes : {3 - score}")
