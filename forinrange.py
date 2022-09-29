#FOR IN RANGE
#Para cada elemento del rango hacer
#instrucciones
#FIN

texto = "Bucle for in range"
texto1 = "Bucle for in range con while"
print("\n" + texto.center(35, "*"))

numero = int(input("\n¿Cúal es el numero que quieres elevar? "))


for potencia in range(0,11):
    resultado =  pow(numero, potencia)
    print(str(numero) + " elevado a " + str(potencia) + " es igual a " + str(resultado))

print("\n" + texto1.center(35, "*"))
potencia = 0
numero = int(input("\n¿Cúal es el numero que quieres elevar? "))
while potencia >= 0 and potencia <11:
    resultado =  pow(numero, potencia)
    print(str(numero) + " elevado a " + str(potencia) + " es igual a " + str(resultado))
    potencia = potencia + 1
