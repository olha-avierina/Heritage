class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print("Marque = ", self.marque)
        print("annee =", self.annee)
        print("Prix =", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.model = model
        self.portes = portes

    def informationVehicule(self):
        super().informationVehicule()
        print("Model =", self.model)
        print("Portes =", self.portes)

    def demarrer(self):
        print("Attention, je roule")


V = Voiture("Honda", "Civic", 2019, 12000)
V.informationVehicule()
V.demarrer()


class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def informationVehicule(self):
        super().informationVehicule()
        print("Nombres de roues =", self.roue)

    def demarrer(self):
        print("Attention, je suis une femme sur un balai")


M = Moto("Yamaha", 2022, 5000)
M.informationVehicule()
M.demarrer()
