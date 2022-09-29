#if
# La sintaxis correcta de un if es
#if
#(indentado 4 espacios)Instrucciones :
#Fin del if(no es necesario declararlo)

cadena = "HOla"
cadena1 = "hola"
print("Estructura IF\n")
print("La palabra descrita en la variable cadena es " + cadena + "\n")

if cadena == "HOla":
    print("La condicion es verdadera\n")

if cadena == "Hola":
    print("La condicion es verdadera\n")

if cadena != "HOLA":
    print("La condicion es verdadera\n")
#if - else
# La sintaxis correcta de un if-else (1 instruccion) es
#if
#(indentado 4 espacios)Instrucciones :
#else
#(indentado 4 espacios)Instrucciones :
#Fin del if(no es necesario declararlo)

print("Estructura IF-ELSE\n")
print("La palabra descrita en la variable cadena es " + cadena + "\n")

if cadena == "Hola":
    print("La condicion es verdadera\n")

else:
    print("La condicion es falsa\n")
#if - else
# La sintaxis correcta de un if-else (varias instrucciones) es
#if condicion1 operador(and u or)logico condicion2
#(indentado 4 espacios)Instrucciones :
#else
#(indentado 4 espacios)Instrucciones :
#Fin del if(no es necesario declararlo)

print("Estructura IF-ELSE con multiples condiciones (operadores logicos)\n")
print("La palabra descrita en la variable cadena es " + cadena1 + "\n")

if cadena1 == "HOLA" or cadena1 == "hola":
    print("La condicion es verdadera\n")

else:
    print("La condicion es falsa\n")
    
#if -elif - else
# La sintaxis correcta de un if-else (varias instrucciones) es
#if condicion1 :
#(indentado 4 espacios)Instrucciones
#elif condicion2 :
#(indentado 4 espacios)Instrucciones
#else:
#(indentado 4 espacios)Instrucciones
#Fin del if(no es necesario declararlo)

print("Estructura IF-ELSE con multiples condiciones\n")
if cadena1 == "HOla":
    print("La condicion es verdadera\n")
elif cadena1 == "hola":
    print("La palabra esta escrita en minusculas\n")
else:
    print("La condicion es falsa\n")
