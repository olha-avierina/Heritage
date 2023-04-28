class Forme:

    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, larguer, hauteur):
        self.largeur = larguer
        self.hauteur = hauteur

    def aire(self):
        print(self.hauteur*self.largeur)


F = Forme()
R = Rectangle(7, 3)
print(R.aire())
