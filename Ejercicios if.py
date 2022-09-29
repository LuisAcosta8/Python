#Numero par o impar
div = 0
m = 0

div = (input("Ingresa el numero que deseas saber si es par o impar: "))
div = int(div)

m = div % 2

if m == 0:
    
    print("El número " + str(div) + " es par")

else:
    print("El número " + str(div) + " es impar")


#Multiplo de 3


div = (input("Ingresa el numero que deseas saber si es multiplo de 3: "))
div = int(div)

m = div % 3

if m == 0:
    
    print("El número " + str(div) + " si es multiplo de 3")

else:
    print("El número " + str(div) + " no es multiplo de 3")
