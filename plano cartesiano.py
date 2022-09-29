import math


class Punto:
    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y
        if X != None and Y != None:
            print("Punto agregado ({},{})".format(X, Y))
        else:
            print("Se agrego un punto en el origen")


    def __str__(self):
        return "({},{})".format(self.x, self.y)


    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("El punto {} esta en el 1er cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("El punto {} esta en el 2do cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("El punto {} esta en el 3er cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("El punto {} esta en el 4to cuadrante".format(self))
        else:
            print("El punto {} esta en el Origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({},{})".format(self, p, p.x - self.x, p.y - self.y))


    def distancia(self, p):
        d = math.srqt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
        
def funcion(a,b):
    c = a+b
    print(c)
