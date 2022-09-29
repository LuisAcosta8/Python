#Librerias
import math
#Titulos
titulo1 = "Área de un rectangulo * arearectangulo(b,h) * "
titulo2 = "Área de un rectangulo * area_rectangulo(b,h) * UDEMY"
titulo3 = "Área de un circulo * areacirculo(r) * "
titulo4 = "Función * relacion(a,b) * "
titulo5 = "Intermedio de dos numeros * intermedio(a,b) * "
titulo6 = "Área de un circulo * areacirculo(r) * "

#Variables
b = 10
h = 15
r = 5

#Programacion de funciones


def arearectangulo(b,h):
    area = b*h
    print(titulo1.center(80,"*"))
    return area
print("El area del rectangulo es de :", arearectangulo(b,h), "metros cuadrados")


def area_rectangulo(b,h):
    return b*h
print(titulo2.center(80,"*"))
print("El area del rectangulo es de :", area_rectangulo(b,h), "metros cuadrados")


def areacirculo(r):
    return math.pi * (r**2)
print(titulo3.center(80,"*"))
print("El área del rectangulo es de :", areacirculo(r), "metros cuadrados")


print(titulo4.center(80,"*"))
x = int(input("Ingresa el primer valor a comparar(a): "))
y = int(input("Ingresa el segundo valor a comparar(b): "))
print("Llama a la función relacion(x,y)")
def relacion(x,y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


def intermedio(n,m):
    return(n + m)/2
    

def recortar(x,y,z):
    if x < y:
        return y
    elif x > z:
        return z
    else:
        return x

numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
pares, impares = separar(numeros)
print(pares)
print(impares)

#def separar(lista):
#    lista.sort()
#    pares = []
#    impares = []
#    for n in lista:
#        if n % 2 == 0:
#            pares.append(n)
#        else:
#            impares.append(n)
#    return pares, impares
#pares, impares = separar(numeros)
#print(pares)
#print(impares)
