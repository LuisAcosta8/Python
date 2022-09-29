#Variables
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
op = int(input("Menú \n1)Suma\n2)Resta\n3)Multiplicación \nOpción: "))
texto = "Opción no valida"
#Programa

if op == 1:
    res = num1 + num2
    print("El resultado de la suma es: " + str(res))
elif op == 2:
     res = num1 - num2
     print("El resultado de la resta es: " + str(res))
elif op == 3:
     res = num1 * num2
     print("El resultado de la multiplicación es: " + str(res))
else:
     print(texto)
