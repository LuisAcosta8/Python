#Pyrhon permite utilizar un acceso a la superclase de forma directa llamado super()
#Permite llamar mas comodamente los metodos o atributos de la superclase sin necesidad de especificar un self
#{}
class Vehiculo():


    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return "Color: {}, Ruedas {}".format(self.color, self.ruedas)

class Coche():


    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return super().__str__() + ", {} km/hr, {} cc".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):


    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas,velocidad, cilindrada)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga = carga


    def __str__(self):
        return super().__str__() + ", {} Kg".format(self.velocidad, self.cilindrada, self.carga)


class Bicicleta(Vehiculo):


   def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


   def __str__(self):
        return super().__str__() + ", {} ".format(self.tipo)
    

class Motocicleta(Bicicleta):


    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        


    def __str__(self):
        return super().__str__() + ", {} km/hr, {} cc".format(self.velocidad, self.cilindrada)


#vehiculos = [
#      Coche("Azul", 4, 150, 1200),
#      Camioneta("Blanco", 4, 180, 1300, 1500),
#      Bicicleta("Verde", 2, "Urbana"),
#      Motocicleta("Negro", 2, "Deportiva", 100, 200)
#        ]


def catalogar(lista):
   for v in lista:
       print("{} {}".format(type(v).__name__, v))
def catalogar():
    pass
