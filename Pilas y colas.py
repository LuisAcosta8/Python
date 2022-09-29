titulo1 = "Pila original"
titulo2 = "Pila Agregando 6 y 7"
titulo3 = "Pila quitando el ultimo elemento que se agrego"
titulo4 = "Muestra del ultimo elemento agregado"
titulo5 = "Muestra de cola vacia"
titulo6 = "Muestra de cola con elementos"
titulo7 = "Agregando Maria y Armando a la cola"
titulo8 = "Quitando el primer elemenot de la lista"

#Pilas
#Colección de elementos ordenados solo permiten añadir un elemento a la pila o sacar un elemento de la pila
#El ultimo en entrar es el primero en salir
#Estructura LIFO(Last in first out)
#Es recomendable poner una variable auxiliar sino queremos perder el numero

pila = [3, 4, 5]
print(titulo1.center(80,"*"))
print(pila)
print(titulo2.center(80,"*"))
pila.append(6)
pila.append(7)
print(pila)
print(titulo4.center(80,"*"))
print(pila.pop())
print(titulo3.center(80,"*"))
print(pila)


#Colas
#Primer elemento en entrar es el primero en salir
#Estructura FIFO(First in, first out)
#Se debe importar la colección
from collections import deque

cola = deque()
print(titulo5.center(80,"*"))
print(cola)

cola = deque(["Luis", "Lety", "Daniela", "Kevin"])
print(titulo6.center(80,"*"))
print(cola)



cola.append("Maria")
cola.append("Armando")
print(titulo7.center(80,"*"))
print(cola)


print(titulo8.center(80,"*"))
cola.popleft() #Solo funciona en las colas
print(cola)
