#Arreglos

arreglo1 = ["Hola", "WEY", "!!!", [1, 2], 5]
INICIO = 0
FIN = -1
INDICE = 2
SALTO = 1

print("\n**********Elementos del arreglo**********\n")

print(arreglo1[0])      #Hola
print(arreglo1[1])      #WEY
print(arreglo1[2])      #!!!
print(arreglo1[3])      #[1, 2]
print(arreglo1[4])      #5
print(arreglo1[-1])     #5
print(arreglo1[-2])     #[1, 2]

print("\n**********Formatear Elementos**********\n")

print("Las cadenas son "+ arreglo1[0] + ", " + arreglo1[1] + " y " + arreglo1[2])
print("Elementos formateados: " + str(arreglo1[3]) + " y " + str(arreglo1[4]))

print("\n**********Número Mágicos**********\n")
print("Posicion Inicial: " + str(INICIO))       
print(arreglo1[INICIO])                         #Hola
print("Posicion Final: " + str(FIN))            
print(arreglo1[FIN])                            #5

print("\n**********Particionando Listas**********\n")
print("Imprimir listas\n")
print(arreglo1)

print("\nParticionando Listas (Inicio:Fin)\n")
print(arreglo1[0:4])
print(arreglo1[0:])

print("\nParticionando Listas (Inicio:Fin:Salto)\n")
print("Número   : lista(INICIO:FIN:SALTO)\n")
print(arreglo1[0:2:1])

print("\nParticionando Listas (Inicio:Fin:Salto)\n")
print("Constantes   : lista(INICIO:INDICE:SALTO)\n") #Definir constantes para mejores practicas
print(arreglo1[INICIO:INDICE:SALTO])


print("\n**********Particion por defecto**********\n")
print("Imprime todos los elementos\n")
print(arreglo1[:])

print("\nImprime desde el numero dos incluyendo el ultimo")
print(arreglo1[2:]) #print(arreglo1[INDICE:])

print("\nImprime un rango lista(inicio:fin:salto)")
print(arreglo1[:4]) #print(arreglo1[:FIN])

print("\nMuestra los datos de uno en uno")
print(arreglo1[::1])    #print(arreglo1[::SALTO])

print("\nMuestra los datos de dos en dos")
print(arreglo1[::2])    #print(arreglo1[::SALTO])
