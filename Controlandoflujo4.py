#Variables
n = int(input("Cantidad de valores a ingresar: "))
suma = 0
#Programa

for x in range(n):
    suma += float(input("Ingresa el valor para la variable " + str(x+1) + (": ")))
print("Se han introducido ", n, " números que en total hacen una suma de ", suma, " y la media es ", suma/n)
