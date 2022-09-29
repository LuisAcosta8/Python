import time
#Declaración de variables
texto = "Bienvenido al menú interactivo"

#Inicio del programa
print(texto.center(70,"*"))
while(True):
    print("¿Qué quieres hacer escribe una opción? \n \t1)Saludar \n \t2)Sumar dos numeros \n \t3)Salir")
    opcion = int(input())
    if opcion == 1:
        print("Hola espero que te la estes pasando bien")
    elif opcion == 2:
        print("Escogiste sumar dos numeros")
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        resultado = num1 + num2
        print("El resultado de tu suma es", resultado)
    elif opcion == 3:
        print("Vuelve pronto")
        time.sleep(5)
        break
    else:
        print("Comando desconocido")

