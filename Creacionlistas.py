#Formas de crear listas

arreglo1 = [] #Lista vacia

arreglo2 = ["Hola", "WEY", "!!!", [1, 2], 5]

arreglo3 = ["Hola"  ,
            "WEY"   ,
            "!!!"   ,
            [1, 2]  ,
            5]

print("\n**********Impresion de las listas**********\n")

print("Arreglo original\n")
print(arreglo2)

print("\nSegundo arreglo\n")
print(arreglo3)

print("\Arreglo vacio\n")
print(arreglo1)

print("\n Arreglo modificado\n")
arreglo2[0] = "Adios"
print(arreglo2)

#Agregar datos a un arreglo
    #arreglo.append(dato) agrega nuevos elementos a una lista de datos // SOBRE EL CODIGO
print("\nAgregar un elemento con arreglo.append(dato)")
arreglo2.append(500)

print("\n Nueva lista\n ")
print(arreglo2)

    #arreglo.extend([DATOS SEPARADOS POR COMAS]) // SOBRE EL CODIGO
print("\nAgregar varios elementos con arreglo.extend([dato1, dato2,...])")
arreglo2.extend([5, 10 ,36 ,81])

print("\n Nueva lista\n ")
print(arreglo2)

    #len(arreglo): Permite saber el numero de elementos que tiene un arreglo  // SOBRE EL CODIGO
print("\n Longitud de una lista:   len(arreglo)\n")
print("Longitud del arreglo2: %d" %(len(arreglo2)))

    #arreglo.remove(valor a remover) Elimina un valor en una lista si es que lo encuentra
print("\nRemover datos de una lista: arreglo.remove(dato)\n")
arreglo2.remove(10)

print("\n Nueva lista\n ")
print(arreglo2)

    #arreglo.pop(Posicion de valor a remover) Elimina un valor en una lista dependiendo de su posicion
print("\nRemover por posición: arreglo.pop(posición)\n")
arreglo2.pop(0)

print("\n Nueva lista\n ")
print(arreglo2)

    #arreglo.index(valor): Devuelve la posicion en que esta el valor
print("\nDevolver la posicion de un valor en un arreglo: arreglo.index(valor)\n")
print("El numero 5 esta en la posicion %d del arreglo2" % (arreglo2.index(5)))

    #arreglo.count(valor): Devuelve las veces que se encuentra el valor en una lista
print("\nValores duplicados\n")
print("\n El numero 5 se encuentra %d de veces en la lista" %(arreglo2.count(5)))

    #arreglo.reverse(): Invierte el contenido de una lista
print("\nLa lista original es:\n")
print(arreglo2)

arreglo2.reverse()

print("\nNueva lista\n")
print(arreglo2)
