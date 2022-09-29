#Ficheros
#Write
from io import open
texto = "Una linea con texto\nOtra linea con texto"
fichero = open("fichero.txt", "w")
fichero.write(texto)

fichero.close()
#Read
fichero = open("fichero.txt", "r")
texto = fichero.read()

fichero.close()
print(texto)

fichero = open("fichero.txt", "r")
texto = fichero.read()

fichero.close()

#Almacenar las lineas del texto en una lista
fichero = open("fichero.txt", "r")
lineas = fichero.readlines()
fichero.close()
print(lineas)

print(lineas[0])
print(lineas[-1])
#Append
fichero = open("fichero.txt", "a")
fichero.write("\nCuarta linea del fichero")
fichero.close()

#No se puede abrir un fichero en modo lectura si este no existe

#readline()
fichero = open("fichero.txt", "r")
l = fichero.readline()
print(l) #1er linea
print(l) #2da linea
print(l) #3er linea
fichero.close()

with open("fichero.txt", "r"):
    for linea in fichero:
        print(linea)
fichero.close()

#Puntero
fichero = open("fichero.txt", "r")
fichero.seek(10)
fichero.read() #Devuelve el contenido del fichero a partir de donde se encuentra el puntero
fichero.seek(0)
fichero.read()
fichero.read(5)
fichero.read()

fichero.seek(0)
texto = fichero.read()
fichero.seek(len(texto)/2)

