# Imprimir del 1 hasta el numero que indique el usuario

inicio = 1
fin=int(input("Hasta que numero deseas imprimir: "))
texto = "Impresion con while"
texto1 = "Impresion de frase con while"
frase = ""


print(texto.center(70,"*"))
while inicio <= fin :
    print(str(inicio))
    inicio = inicio + 1

#Contar palabras de una frase que se introduzca


opcion = "Si"
frase = ""
contador = 1

print(texto1.center(70,"*"))
while opcion == "Si" or opcion == "si" or opcion == "SI" or opcion == "sI":
    frase = (input("Ingresa la palabra # " + str(contador)))
    contador = contador + 1
    opcion = (input("¿Quieres agregar una palabra a tu frase? "))

   
print("El numero de palabras que contiene tu frase es de " + str(contador - 1))
