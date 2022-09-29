from time import sleep
#Clases

class Coche():
    #estado inicial (Propiedades que comparten todos los objetos)
    """largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    """
    #Constructor de clase
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    #Encapsular propiedades para que nadie pueda modificarlas para esto se utilizan __ antes del nombre de esta

#Metodos


    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            chequeo = self.__chequeo_interno()
        if self.__enmarcha == True and chequeo == True:
            print("El coche esta en marcha")
        elif self.__enmarcha == True and chequeo == False:
            print("Algo ha ido mal en el chequeo, no se puede arrancar")
        else:
            return "El coche esta parado"
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoChasis, " y un lardo de ", self.__largoChasis)
    
    #Encapsular el siguiente metodo para que no se pueda acceder desde fuera de la clase
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False
        

#Crear instancias de clase u objetos


miCoche = Coche()
#Ya no es necesario este codigo pues el metodo estado devuelve todas estas lineas
"""
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas,"ruedas")
"""
miCoche.arrancar(True)

miCoche.estado()

#Crear segundo objeto
print("Segundo objeto")

miCoche2 = Coche()
#Ya no es necesario este codigo pues el metodo estado devuelve todas estas lineas
"""print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene ", 2.ruedas,"ruedas")
"""

print(miCoche2.arrancar(False))
miCoche2.__ruedas = 5 #El valor de la propiedad no cambia
miCoche2.estado()
#miCoche.__chequeo_interno() **dira que no tiene este metodo

#Modificar alguna propiedades
#miCoche.enmarcha = "True"
#print(miCoche.enmarcha) utilizar encapsulamiento para que no se pueda acceder a la variable
#print(miCoche.chequeo interno())  sino estuviera los guiones bajos se puede accesar dede aqui

#Se deben encapsular metodos y variables cuando el objeto o la clase lo necesite

#HERENCIA
#Clase1 ---- clase padre o super clase
#clase2 ---- Subclase de clase1 y superclase de clases posteriores
#clase3 ----
#Sirve para reutilizar codigo si se crean objetos similares
#¿Que caracteristicas tienen en comun?
#¿Que metodos o comportamientos tienen en comun?
class Vehiculos():

    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

#Herencia clase nombre(de quien hereda)


#class Moto():
#    pass
#mimoto = Moto("Honda", "CBR1000RR")
#mimoto.estado() **Sino se hereda nada aria error porque la clase moto no acepta parametros y no tiene constructor 


class Moto(Vehiculos):
    hcaballito = False
    #Metodo propio de la clase
    def caballito(self):
        self.hcaballito = True
    #Sobre escritura de metodos---Se debe sobreescribir el metodo pues este es diferente al metodo estado de la clase vehiculo    
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\nCaballito:", self.hcaballito)

mimoto = Moto("Honda", "CBR1000RR")
#mimoto.caballito()
mimoto.estado()

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if self.cargado == True:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    
mifurgo = Furgoneta("Peugeot", "Rifter")
mifurgo.estado()
print(mifurgo.carga(False))
#Herencia simple y multiple

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)


        
        self.autonomia = 100

    def cargar(self, bateria):
        while bateria < 99:
            sleep(1)
            bateria +=1
            print(str(bateria)+"%")
        else:
            print("100% Bateria cargada")
#Herencia multiple siempre se toma el constructor de la clase que se haya colocado primero como argumento
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

mibicie = BicicletaElectrica("Milano","Legend")
print("bicicleta")
mibicie.estado()

#Funcion super() para sobreponer una clase sobre otra, donde se coloque llamara a la clase padre