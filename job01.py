class Personne:
    def __init__(self, age=14):
        self.age = age

    def affisherAge(self):
        print("J`ai", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, newage):
        self.age = newage


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation des objets
pers = Personne()
el = Eleve()
prof = Professeur("Math")

# Affichage de l'âge par défaut de l'élève
eleve.affichageAge()
