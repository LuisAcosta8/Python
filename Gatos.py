class Gato:
    especie = "mamifero"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.alimentos = []

    def verEtapaDeVida(self):
        if self.edad > 1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")

    def esAlimentoFavorito(self, alimento):
        return alimento in self.alimentos
