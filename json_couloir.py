import sys
import json

nom_fichier = sys.argv[1]

with open(nom_fichier) as f:
    data = json.load(f)

# créer une liste
liste = [c['SOLIFE']['url'] for c in data if 'SOLIFE' in c]

# parcours avec un générateur (pas de création de liste)
for x in (c['SOLIFE']['url'] for c in data if 'SOLIFE' in c):
    print(x)

# parcours avec un filtre (pas de création de liste)
for x in filter(lambda c : "SOLIFE" in c, data):
    print(x['SOLIFE']['url'])

# parcours old school
for c in data:
    if 'SOLIFE' in c:
        print(c['SOLIFE']['url'])