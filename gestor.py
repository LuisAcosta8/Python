from io import open
import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        
    def __str__(self):
        return "{}\nVida:{}\nAtaque:{}\nDefensa:{}\nAlcance:{}".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)
    
    
class Gestor:
    personajes = []
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        for pTem in self.personajes:
            if pTem.nombre == p.nombre:
                return
            else:
                self.personajes.append(p)
                self.guardar()
                
    def borrar(self, nombre):
        for pTem in self.personajes:
            if pTem.nombre == nombre:
                self.personajes.remove(p)
                self.guardar()
                print("\n Përsonaje borrado {}".format(nombre))
                return
    
    def mostrar(self):
        if len(self.personajes) == 0:
            print("Lista de personajes vacia")
            return
        else:
            for p in self.personajes:
                print(p)

    def cargar(self):
        fichero = open("catalogo.pckl", "a+")
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero esta vacio")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open("personajes.pckl", "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()


g = Gestor()
g.mostrar()
g.agregar(Personaje("Caballero",4,2,4,2))
g.agregar(Personaje("Guerrero",2,4,2,4))
g.agregar(Personaje("Arquero",2,4,1,8))
g.mostrar()
#p = Personaje("Pikachu", 8, 9, 5, 10)
#p = Personahe
