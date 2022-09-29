#Colecciones
#sub clase de diccionario
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]

#[]
#{}
print("Lista: ", l)
print(Counter(l))              #Cuenta las veces que se repite un caracter y te regresa el numero y veces en forma de diccionario


p = "PalabraP"

print("Cadena", p)              #Distingue entre minusculas y mayusculas
print(Counter(p))


animales = "Gato Perro Canario Perro Canario Perro"

print(animales)
print(Counter(animales))


print("Lista animales: ", animales.split())
print(Counter(animales.split()))

c = Counter(animales.split())

print(c.most_common(1))         #El más comun
print(c.most_common(2))         #Los dos más comunes

l = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]

c = Counter(l)
print("Se pueden tratar como diccionarios")

print("Items:",c.items())

print("Keys:",c.keys())

print("Values:",c.values())

print("Suma de valores:",sum(c.values()))


print(list(c))

print(dict(c))

print(set(c))

"""
d = {}
d["algo"]      Da error si se intenta crear un diccionario asi xq solo se da la llave pero no el valor      
"""
#Pero se soluciona con una coleccion que da un valores por defecto

from collections import defaultdict

d = defaultdict(float)              #Se tiene q indicar en tipo de dato para los valores
d["Algo"]
print("Default Dict:",d)

d = defaultdict(str)
d["Algo"]
print(d)
