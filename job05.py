
class Forme:
    def aire(self):
        return 0


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        print(3.14*(self.radius**2))


C = Cercle(3)
C.aire()
