#Declaracion de variables
i = int(input("Inserta el numero de filas que necesitas: "))
j = int(input("Inserta el numero de columnas que necesitas: "))
matriz=[]

#for filas in range(i):
#    matriz.append([0]*j)
#print(matriz)

for filas in range(i):
    matriz.append([0]*j)

for filas in range(i):
    for columnas in range(j):
        matriz[filas][columnas] = int(input("Ingresa el valor para %d, %d: " %(filas,columnas)))
print(matriz)
