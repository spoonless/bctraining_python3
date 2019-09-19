import sys
import json
import configparser

fichier_source = sys.argv[1]
fichier_dest = sys.argv[2]

def lower_dict_key(d):
    return {k.lower(): v for k, v in d.items()}


with open(fichier_source) as f:
    data = json.load(f, object_hook=lower_dict_key)


def extraire_couloir(c):
    besoin = c["besoin"]
    nom_couloir = besoin.split(sep='-', maxsplit=1)
    numero_couloir = nom_couloir[0].strip()
    return numero_couloir


dict_solife = {extraire_couloir(c): c['solife']['url'] for c in data if 'solife' in c}

config = configparser.ConfigParser()
config.read(fichier_dest)
num_couloir = config['config']['couloir']

if num_couloir in dict_solife:
    config['config']['solife'] = dict_solife[num_couloir]

with open(fichier_dest, mode="w") as f:
    config.write(f)
