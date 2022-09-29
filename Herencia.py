#Herencia
#class producto:


#    def __init__(self, referencia, tipo, nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):


#        self.referencia = referencia
#        self.tipo = tipo
#        self.nombre = nombre
#        self.pvp = pvp
#        self.descripcion = descripcion
#        self.productor = productor
#        self.distribuidor = distribuidor
#        self.isbn = isbn
#        self.autor = autor


#adorno = Producto("000A", "Adorno", "Vaso adornado", 15, "Vaso de porcelana con dibujos")


#No hay un orden o una logica para mezclar productos se debe dividir en cases y subclases
#La jerarquia que ocupan todos los elementos
class Producto:


    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion


    def __str__(self):
        return """\
Referencia \t{}
Nombre \t\t{}
PVP \t\t{}
Descripción \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)
    

class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
Referencia \t{}
Nombre \t\t{}
PVP \t\t{}
Descripción \t{}
Productor \t{}
Distribuidor \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


class Libros(Producto):
     isbn = ""
     autor = ""


     def __str__(self):
        return """\
Referencia \t{}
Nombre \t\t{}
PVP \t\t{}
Descripción \t{}
ISBN \t\t{}
Autor \t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)
     
