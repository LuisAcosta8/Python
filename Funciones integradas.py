titulo1 = "Concatenación de numeros * str()* "
titulo2 = "Números binarios * bin(numero) * "
titulo3 = "Números hexadecimal * hex(numero) * "
titulo4 = "Binario a entero* int('numero',2) * "
titulo5 = "Hexadecimal a entero* int('numero',16) * "
titulo6 = "Valor absoluto * abs(numero) * "
titulo7 = "Redondear un numero <<-.4 .5 ->> * round(numero) * "
titulo8 = " * eval(numeros) * "
titulo9 = "Longitud de un argumento * len(argumento) * "
titulo10 = " * help() * "


#Funciones integradas
n = "10"
f = "10.5"
c = "Un texto y el numero " + str(10)
x = -10
y = 10
numero = 5.5
texto = "Una cadena"


print(titulo1.center(80,"*"))
print(c)


print(titulo2.center(80,"*"))
print("Número 10")
print("Binario: ", bin(10))


print(titulo3.center(80,"*"))
print("Número 15")
print("Hexadecimal: ", bin(15))


print(titulo4.center(80,"*"))
print("Binario 0b1010")
print("Entero: ", int('0b1010',2))


print(titulo5.center(80,"*"))
print("Hexadecimal 0xf")
print("Entero: ", int('0xf',16))


print(titulo6.center(80,"*"))
print("x = ", x)
print("y = ", y)
print("El valor absoluto de x es ", abs(x))
print("El valor absoluto de y es ", abs(y))


print(titulo7.center(80,"*"))
print("Número es = ", numero)
print("Número redondeado: ", round(numero))


print(titulo8.center(80,"*"))
print(eval('2+5'))


print(titulo9.center(80,"*"))
print("texto = Una cadena")
print(len(texto))


print(titulo10.center(80,"*"))
print("Invoca la ayuda de python")
help()
