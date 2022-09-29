#[]
titulo1 = "Tupla original"
titulo2 = "Elementos tupla 1er elemento"
titulo3 = "Elementos tupla último elemento"
titulo4 = "Del Segundo elemento al último (Se comienza a contar desde 0)"
titulo5 = "Elemento 0 del arreglo que se encuentra en la posición 2"
titulo6 = "Longitud de la Tupla"
titulo7 = "Longitud de un elemento entro de la tupla"
titulo8 = ".index para buscar un elemento dentro de una tupla"



#Tuplas
#Colecciones parecidas a las listas pero con tienen valores inmutables
#Sintaxis                tupla = ()
#Ejemplo                 tupla = ("hola", 8, 15, ["wey","como", 8])

tupla = (100, "Hola", [1, 2, 3, 4], -50)
print(titulo1.center(80,"*"))
print(tupla)


print(titulo2.center(80,"*"))
print(tupla[0])


print(titulo3.center(80,"*"))
print(tupla[-1])


print(titulo4.center(80,"*"))
print(tupla[2:])


print(titulo5.center(80,"*"))
print(tupla[2][0])


print(titulo6.center(80,"*"))
print(len(tupla))


print(titulo7.center(80,"*"))
print(len(tupla[2]))


# .index para buscar un elemento y saber su posición pero devolvera un error si no lo encuentra
print(titulo8.center(80,"*"))
print(tupla.index(100))
print(tupla.index(X))


tupla[0] = 50           #No se pueden modificar
print(tupla)




