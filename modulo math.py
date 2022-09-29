import math
#round
pi = 3.14159 #REDONDEA A LA BAJA PORQUE EL PRIMER DECIMAL ES MENOR A 5
print(round(pi))
p = 3.5      #REDONDEA AL NUMERO PROXIMO MAS ALTO
print(round(p))
#math.floor() REDONDEA EL NUMERO AL PROXIMO MAS BAJO
print(math.floor(3.9))
#mat.ceil() REDONDEA A LA ALTA
print(math.ceil(3.00002))
#abs
print(abs(-14))
#sum
n = [1,2,3,4,5]
print(sum(n))
#math.fsum() #Devuelve la sumatoria en  tipo flotante
print(math.fsum(n))
#math.trunc() Devuelve el numero sin decimales
print(math.trunc(100.25789))
#math.pow(num1, num2) Devuelve la raiz del num1 elevado al num2
print(math.pow(2, 3))
#math.sqrt() Devuelve la raiz del numero
print(math.sqrt(9))
#Constantes
print(math.pi)
print(math.e)
