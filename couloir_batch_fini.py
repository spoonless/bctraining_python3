import sys
import json
import configparser

def print_help():
    """Affiche le message d'aide"""
    print("Pour utiliser le programme:", file=sys.stderr)
    print(f"\t{sys.argv[0]} SOURCE DEST", file=sys.stderr)
    sys.exit(1)


def get_json(filepath):
    """Charge un fichier json sous la forme d'un dictionnaire.
       Les clés du dictionnaire sont normalisées en minuscules.
    """
    def lower_dict_key(d):
        return {k.lower(): v for k, v in d.items()}


    with open(filepath) as f:
        return json.load(f, object_hook=lower_dict_key)


def get_url_solife_dict(json):
    """Extrait un dictionnaire dont la clé est le numéro de couloir et
       la valeur est l'URL de SOLIFE
    """
    def extraire_numero_couloir(c):
        besoin = c["besoin"]
        nom_couloir = besoin.split(sep='-', maxsplit=1)
        numero_couloir = nom_couloir[0].strip()
        return numero_couloir


    return {extraire_numero_couloir(c): c['solife']['url'] for c in json if 'solife' in c}


def remplacer_config(configfile, dict_solife):
    """Remplace l'URL de SOLIFE dans un fichier de configuration INI"""
    config = configparser.ConfigParser()
    config.read(configfile)
    num_couloir = config['config']['couloir']

    if num_couloir in dict_solife:
        config['config']['solife'] = dict_solife[num_couloir]

    with open(configfile, mode="w") as f:
        config.write(f)


if len(sys.argv) != 3:
    print_help()

fichier_source = sys.argv[1]
fichier_dest = sys.argv[2]

conf_json = get_json(fichier_source)
dict_solife = get_url_solife_dict(conf_json)
remplacer_config(fichier_dest, dict_solife)

