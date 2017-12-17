class Jardinier:

    def __init__(self, nom, prenom, addresse):

        self.nom = nom
        self.prenom = prenom
        self.addresse = addresse
        self.points = 0


class Jardin:

    def __init__(self, proprietaire, location, taille, arbres, buissons, herbes):

        self.proprietaire = proprietaire
        self.location = location
        self.taille = taille
        self.arbres = arbres #dictionnaire'objet Arbre et location
        self.buissons = buissons #dictionaire d'objet buisson et ""
        self.herbes = herbes #dictionnaire d'objet herbes et ""

    def ajout_arbre(self, nom_scientifique, location):



class Proprietaire:

    def __init__(self, nom, prenom,):

        self.nom = nom
        self.prenom = prenom
        self.points = 0

class Arbre:

    def __init__(self, nom_scientifique, nom_commun, taille):

        self.nom_scientifique = nom_scientifique
        self.nom_commun = nom_commun
        self.taille = taille


class Crataegus_monogyna(Arbre):

    def __init__(self, taille):

        Arbre.__init__(self, 'Crataegus_monogyna', [aubepine_a_un_style,], taille)
