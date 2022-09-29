titulo1 = "Conjunto"
titulo2 = "Añadiendo h, z, 58, a"
titulo3 = "Añadiendo Luis y Hector"
titulo4 = "Lista vs Conjunto"
titulo5 = "Lista"
titulo6 = "Conjunto"
titulo7 = "Convertir una lista en un conjunto"
titulo8 = "Refran"
conjunto = {1, 2, 3}


#Conjuntos
#Colecciones desordenadas de elementos unicos, prueba de pertenencia a grupos y eliminacion de datos repetidos
###Sintaxis conjunto vacio ---> conjunto = ()  conjunto = {}
#Ejemplo                        conjunto = {1, 2, 3}
#{}

print(titulo1.center(80, "*"))
print(conjunto)


#Si se añaden mas valores a un conjunto no se lleva un orden como en una lista
conjunto.add("h")
conjunto.add("z")
conjunto.add(58)
conjunto.add("a")
print(titulo2.center(80, "*"))
print(conjunto)


#Añadiendo Luis y Hector
grupo = {"Hector", "Juan", "Mario"}
grupo.add("Luis")
grupo.add("Hector")
print(titulo3.center(80, "*"))
print(grupo)

print(titulo4.center(80, "*"))
print(titulo5.center(80, "*"))
l = [1, 2, 3, 4, 4, 8, 8]
print(l)


print(titulo6.center(80, "*"))
c = {1, 2, 3, 4, 4, 8, 8}
print(c)



print(titulo7.center(80, "*"))
co = set(l)             #Convertir una lista en un conjunto, al hacer esto se eliminan los valores repetidos de la lista
print(co)


print(titulo8.center(80, "*"))
s = "Al pan pan y al vino vino"
s = set(s)
print(s)


#Para eliminar un registro se utiliza conjunto.remove("registro")
