titulo1 = "Alineación de datos"
titulo2 = "Formateo número con espacios"
titulo3 = "Formateo números con ceros"
titulo4 = "Números flotantes con espacios"
titulo5 = "Recortar números flotantes a dos decimales"
titulo6 = "Alineacion de números flotantes"
titulo7 = "Alineacion de números flotantes rellenados con ceros"
titulo8 = ".format simplicaficado"


#Salida de datos
print(titulo1.center(80,"*"))
print("{:>30}".format("palabra")) #Alineación a la derecha con 30 caracteres
print("{:30}".format("palabra")) #Alineación a la izquierda con 30 caracteres
print("{:^30}".format("palabra")) #Alineación a la centro con 30 caracteres
print("{:.3}".format("palabra")) #Truncamiento de palabras
print("{:>30.3}".format("palabra")) #Alineación a la derecha con truncamiento 3 caracteres


#Formateo de números enteros; rellenar con espacios
print(titulo2.center(80,"*"))
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))


#Formateo de números enteros; rellenar con ceros
print(titulo3.center(80,"*"))
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))


#Formateo de números flotantes, rellenados con espacios
print(titulo4.center(80,"*"))
print("{}".format(3.1415926))
print(titulo5.center(80,"*"))
print("{:.3f}".format(3.1415926))
print("{:.3f}".format(12.5))
print(titulo6.center(80,"*"))
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(112.5))
print(titulo7.center(80,"*"))
print("{:07.3f}".format(3.1415926))


#Format simplificado
print(titulo8.center(80,"*"))
nombre = "Héctor"
cadena = "Hola {}".format(nombre)
#Podemos indicar que la cadena está formateada añadiendo f delante y pasando directamente las variables o datos interpretados:
print(cadena)
nombre = "Héctor"
cadena = f"Hola {nombre}"
print(cadena)

#Como véis es muy útil y permite ahorrarnos algo de código.
