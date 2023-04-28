class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        print(self.longueur*2+self.largeur*2)

    def surface(self):
        print(self.longueur*self.largeur)

    def get_longueur(self):
        return self.longueur

    def set_longueur(self, newlonguer):
        self.longueur = newlonguer

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, newlarger):
        self.largeur = newlarger


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        print((self.longueur*self.largeur*self.hauteur))


r = Rectangle(15, 5)
r.perimetre()
r.surface()
p = Parallelepipede(15, 5, 2)
p.volume(15, 5, 2)
