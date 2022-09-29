#Operadores aritmeticos
#Simbolo        Significado             Ejemplo             Resultado
# +             Suma                    a = 10 + 5          a es 15
# -             Resta                   a = 10 - 5          a es 5
# *             Multiplicacion          a = 10 * 5          a es 50
# **            Exponente               a = 2 ** 3          a es 8
# /             Division                a = 12.5 / 2        a es 6.25 
# //            Division entera         a = 12.5 / 2        a es 6.0
# %             Modulo                  a = 27 % 4          a es 3

ac = 0
at = 0
aci = 0
l = 0
bt = 0
ht = 0
r = 0
pi = 3.1416
celsius = 0
f = 0

print("1)Area de un cuadrado")
print("2)Area de un triangulo")
print("3)Area de un circulo")
print("4)Convertir °F a °C")
l = (input("Ingresa el lado del cuadrado del cual deseas calcular su área: "))
l = int(l)
bt = (input("Ingresa la base del triangulo del cual deseas calcular su área: "))
bt = int(bt)
ht = (input("Ingresa la altura del triangulo del cual deseas calcular su área: "))
ht = int(ht)
r = (input("Ingresa el radio del circulo del cual deseas calcular su área: "))
r = int(r)
f = (input("Ingresa los °F que quieres convertir a °C: "))
f = int(f)
ac = pow(l, 2)
at = ((bt*ht)/2) 
aci= (pi * pow(r, 2))
celsius = (f - 32) * 5/9
print("El área del cuadrado es: " + str(ac))
print("El área del triangulo es: " + str(at))
print("El área del circulo es: "+ str(aci))
print("°C= " + str(celsius))
