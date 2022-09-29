class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)
    

class Coche():

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return "color {}, {} km/hr, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada)


###El inconveniente de ir sobreescribiento es que tenemos que volver a escribir el codigo de la superclase y luego el especifico de la subclase###

