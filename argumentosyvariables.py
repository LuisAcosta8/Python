titulo1 = "Paso por valor "
titulo2 = "Paso por referencia"
titulo3 = "Doble asignacion"
titulo4 = "Sin modificar una lista"
titulo5 = "Argumentos indeterminados(Tupla)"
titulo6 = "Argumentos indeterminados como diccionario(Diccionario)"
titulo7 = "Superfuncion con un poco de todo"

#Argumentos y parametros

def resta(a,b):
    return a-b


def res(a=None , b=None):
    if a == None or b == None:
        print("Error. debes enviar dos numeros a la función")
        return
    return a-b

#Argumentos por valor y referencia


print(titulo1.center(80,"*"))
#numero es una copia del numero externo y no le afecta nada lo q se haga dentro de la funcion
def doblarvalor(numero):
    numero*=2                   #Este numero 
n = 10
doblarvalor(n)
print(n)


#Las listas hacen referencia a la variable original
print(titulo2.center(80,"*"))
def doblarvalores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2

ns = [10, 50, 100]
doblarvalores(ns)
print(ns)


#Como en el primer ejemplo pero se vuelve a asignar a la variable
print(titulo3.center(80,"*"))
def doblarvalor(numero):
    return numero*2

n = 10
n = doblarvalor(n)              #Se vuelve a asignar el valor ya retornado
print(n)


#se puede evitar que se modifique una lista si se hace una copia
print(titulo4.center(80,"*"))
def doblarvalores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2

ns = [10, 50, 100]
doblarvalores(ns[:])                    #Slicing
print(ns)

###############Argumentos indetermidanos################
print(titulo5.center(80,"*"))                           #Tupla
def indeterminadosposicion(*args):
    print(args)
indeterminadosposicion(5, "Hola", [1, 2, 3, 4, 5])
#for arg in args:
    #print(arg) para recorrer los argumentos uno a uno


#kwargs 
print(titulo6.center(80,"*"))                           #Diccionario
def indeterminadosnombre(**kwargs):
    print(kwargs)                                       
indeterminadosnombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])


print(titulo6.center(80,"*"))                           #Diccionario
def indeterminadosnombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," : ", kwargs[kwarg])                                                              
indeterminadosnombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])

#Superfunción con un poco de todo
print(titulo7.center(80,"*"))
def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es ", t)
    for kwarg in kwargs:
        print(kwarg, " : ", kwargs[kwarg])
super_funcion(15, 48, 115, 120.569, 30, Nombre = "Luis", Apellido = "Acosta", Edad = 27)
#[]
