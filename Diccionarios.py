titulo1 = "Diccionario vacio que muestra el tipo de dato"
titulo2 = "Colores"
titulo3 = "Modificar un registro"
titulo4 = "Borrando el azul"
titulo5 = "Edades"
titulo6 = "Edades+=1"
titulo7 = "Suma edades"
titulo8 = "Usando ciclo for para nombres"
titulo9 = "Usando ciclo for para edades"
titulo10 = "Usando ciclo for para nombres y edades(Forma incorrecta)"
titulo11 = "Items"
titulo12 = "Coleccion de datos"
titulo13 = "Agregando dos registros más"
titulo14 = "Utilizando For en una coleccion de datos"



#Diccionarios
#Estructura mapeada, donde cada elemento de la coleccion se encuentra identificada con una clave unica (Desordenada)
#Sintaxis       Diccionario vacio ---> vacio = {} []
#Ejemplo


print(titulo1.center(80, "*"))
vacio = {}
print(type(vacio))


print(titulo2.center(80, "*"))
colores = {"Amarillo":"Yellow", "Azul":"Blue", "Verde":"Green"}
print(colores, "Original")
print(colores["Azul"])


print(titulo3.center(80, "*"))
colores["Amarillo"] = "White"
print(colores)


print(titulo4.center(80, "*"))
del(colores["Azul"])
print(colores)


print(titulo5.center(80, "*"))
edades = {"Hector":27, "Juan":26, "Kevin":14}
print(edades)


#Aumendando un año a algun registro
print(titulo6.center(80, "*"))
edades["Kevin"]+=1
print(edades)


#Sumando valores
print(titulo7.center(80, "*"))
print(edades["Hector"] + edades["Juan"])


print(titulo8.center(80, "*"))
for edad in edades:
    print(edad)


print(titulo9.center(80, "*"))
for clave in edades:
    print(edades[clave])


print(titulo10.center(80, "*"))
for clave in edades:
    print(clave, edades)


print(titulo11.center(80, "*"))
for clave,valor in edades.items():
    print(clave,valor)


print(titulo12.center(80, "*"))
personajes = []
p = {"Nombre":"Son Goku(Kakarotto)", "Raza":"Sayayin", "Fecha de nacimiento":"736"}
personajes.append(p)
print(personajes)


print(titulo13.center(80, "*"))
p = {"Nombre":"Son Gohan", "Raza":"Terricola/Sayayin", "Fecha de nacimiento":"757"}
personajes.append(p)
p = {"Nombre":"Milk", "Raza":"Humana", "Fecha de nacimiento":"737"}
personajes.append(p)
print(personajes)


print(titulo14.center(80, "*"))
for p in personajes:
    print(p["Nombre"], p["Raza"])
