#Variables
num = 0
titulo = "Suma de numeros pares entre 0 y 100"
resultado = 0
aux = 0
titulo2 = "Más facil y sin imprimir todos los números"

#Programa
print(titulo.center(80,"*"))
for num in range(0, 101, 2):
    if num % 2 == 0:
        aux = num
        resultado = resultado + aux
    num = num + 1
    #print(resultado) para imprimir todos los resultados
print(resultado) #Para imprimir solo el ultimo
    
#MásFacil
print(titulo2.center(80,"*"))
suma = sum(range(0, 101, 2))
print(suma)
