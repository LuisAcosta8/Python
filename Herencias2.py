#Herencias2
class Vehiculo():


    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return "Color: {}, Ruedas {}".format(self.color, self.ruedas)

class Coche():


    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/hr, {} cc".format(self.velocidad, self.cilindrada)
    

