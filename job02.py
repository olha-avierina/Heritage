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
    def __init__(self, matiereEnseignee, age=40):
        self.matiereEnseignee = matiereEnseignee
        self.age = age

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation des objets
personne = Personne()
eleve = Eleve()
# Faire dire bonjour à l'élève
eleve.bonjour()

# Envoyer l'élève en cours et redéfinir son âge à 15 ans
eleve.modifierAge(15)
eleve.allerEnCours()
professeur = Professeur("Math", 40)

# Faire dire bonjour au professeur et commencer le cours
professeur.bonjour()
professeur.enseigner()
