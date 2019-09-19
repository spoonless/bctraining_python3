'''
Created on 18 sept. 2019

@author: david
'''

class Vehicule:

    def __init__(self):
        self.klaxon = "tût tût"

    def klaxonner(self):
        print(self.klaxon)

class Voiture(Vehicule):
    """Ceci est la doc"""

    __slots__ = ["_compteur_kilometrique", "couleur"]

    def __init__(self, compteur_kilometrique=0):
        super().__init__()
        self._compteur_kilometrique = compteur_kilometrique

    def rouler(self, nb_kilometres):
        self._compteur_kilometrique += nb_kilometres

    @property
    def neuve(self):
        return self._compteur_kilometrique == 0

    @property
    def compteur_kilometrique(self):
        return self._compteur_kilometrique

    def klaxonner(self):
        print("pouët pouët")

class BoiteDeVitesseError(Exception):
    pass

class BoiteDeVitesse:

    def __init__(self, rapports=6):
        if 1 > rapports > 21:
            raise ValueError("Le nombre de rapports doit être compris entre 1 et 21 !")

        self.rapports = rapports
        self.rapport_courant = 0

    def monter_rapport(self, inc_rapport=1):
        if inc_rapport not in (1, 2):
            raise BoiteDeVitesseError("Il n'a pas possible de monter de plus de deux rapports")

        self.rapport_courant = min(self.rapports,
                                   self.rapport_courant + inc_rapport)

    def retrograder(self, dec_rapport=1):
        if dec_rapport in (1, 2):
            self.rapport_courant = max(0, self.rapport_courant - dec_rapport)

    @property
    def au_point_mort(self):
        return self.rapport_courant == 0

    @property
    def en_marche_arriere(self):
        return self.rapport_courant == -1

    def passer_marche_arriere(self):
        if self.au_point_mort:
            self.rapport_courant = -1

    def __eq__(self, bdv):
        if not isinstance(bdv, BoiteDeVitesse):
            return False
        return self.rapports == bdv.rapports

    def __str__(self):
        return f"Boite de vitesse avec {self.rapports} rapports"
