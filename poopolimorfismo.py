#Polimorfismo
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando ocho ruedas")

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()


mivehiculo = Moto()
mivehiculo.desplazamiento()


mivehiculo2 = Coche()
mivehiculo2.desplazamiento()


mivehiculo3 = Camion()
mivehiculo3.desplazamiento()


#Gracias al polimorfismo Un objeto puede tener la capacidad de cambiar de forma y de comportarse de diferente forma dependiendo del contexto

desplazamientoVehiculo(mivehiculo3)


"""
def *funcion*(objeto):
    valordelobjeto.**otrafuncion()**
*funcion*(mivehiculo3)
"""
#al llamar a la funcion desplazamientoVehiculo y pasarle el objeto como argumento el objeto se 

        
    