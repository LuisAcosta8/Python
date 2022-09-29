#Contador
#variable = variable +/- constante
#Acumulador
#acumulador = acumulador +/- variable

#break
#Se utiliza break para romper el ciclo


#Sentencia WHILE
#while condicion:
#instruccion
#Fin


tabla = 11
numero = 1
resultado = 0

texto = "TABLA DE MULTIPLICAR"

print("\n" + texto.center(35, "*") + "\n")

while numero < 11:
    resultado = tabla * numero

    print(str(tabla) + " x " + str(numero) + " = " + str(resultado))
    numero = numero + 1
