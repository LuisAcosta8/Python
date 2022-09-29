Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: C:\Users\LaPape\Documents\python\Herencia.py ============

============== RESTART: C:\Users\LaPape\Documents\python\Herencia.py =============
alimento = Alimento(2035, "Bottella de aceite de oliva", 5, "250ml")
libro = Libros(2036, "Cocina Mediterránea", 9, "Recetas sanas y buenas")
alimento.productor = "La aceitera"
alimento.distribuidor = "Distribuciones SA"
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(alimento)
Referencia 	2035
Nombre 		Bottella de aceite de oliva
PVP 		5
Descripción 	250ml
Productor 	La aceitera
Distribuidor 	Distribuciones SA
print(libro)
Referencia 	2036
Nombre 		Cocina Mediterránea
PVP 		9
Descripción 	Recetas sanas y buenas
ISBN 		0-123456-78-9
Autor 		Doña Juana
ad = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con árboles")
print(ad)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		15
Descripción 	Vaso de porcelana adornado con árboles
productos = [ad, alimento, libro]
print(productos)
[<__main__.Adorno object at 0x00000189614267D0>, <__main__.Alimento object at 0x0000018961426860>, <__main__.Libros object at 0x0000018961427550>]
for p in productos:
    print(p,"\n")

    
Referencia 	2034
Nombre 		Vaso adornado
PVP 		15
Descripción 	Vaso de porcelana adornado con árboles 

Referencia 	2035
Nombre 		Bottella de aceite de oliva
PVP 		5
Descripción 	250ml
Productor 	La aceitera
Distribuidor 	Distribuciones SA 

Referencia 	2036
Nombre 		Cocina Mediterránea
PVP 		9
Descripción 	Recetas sanas y buenas
ISBN 		0-123456-78-9
Autor 		Doña Juana 


for p in productos:
    print(p.referencia, p.nombre)

    
2034 Vaso adornado
2035 Bottella de aceite de oliva
2036 Cocina Mediterránea
#Si se intenta acceder al autor o productor no funciona porque esos campos no son parte de la clase principal
for p in producto:
    print(p.autor)

    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for p in producto:
NameError: name 'producto' is not defined. Did you mean: 'Producto'?
#isinstance
#En este caso comprueba a que clase pertenece el objeto, tambien puede comprobar que tipo de dato es
for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia, p.nombre)
    elif(isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.productor)
    elif(isinstance(p, Libros)):
        print(p.referencia, p.nombre, p.ibsn)

        
2034 Vaso adornado
2035 Bottella de aceite de oliva La aceitera
Traceback (most recent call last):
  File "<pyshell#32>", line 7, in <module>
    print(p.referencia, p.nombre, p.ibsn)
AttributeError: 'Libros' object has no attribute 'ibsn'
for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia, p.nombre)
    elif(isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.productor)
    elif(isinstance(p, Libros)):
        print(p.referencia, p.nombre, p.isbn)

        
2034 Vaso adornado
2035 Bottella de aceite de oliva La aceitera
2036 Cocina Mediterránea 0-123456-78-9
#Modificar atributos
def rebajarproducto(p,rebaja):
    #Devuelve un producto con una rebaja en porcentaje#
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

al_rebajado = rebajarproducto(ad)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    al_rebajado = rebajarproducto(ad)
TypeError: rebajarproducto() missing 1 required positional argument: 'rebaja'
al_rebajado = rebajarproducto(ad, 20)
print(al_rebajado)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
print(ad)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
#El problema es que se copia por referencia y baja el precio aunque se copie en una nueva variable
l = [1,2,3,4]
l2 = [:]
SyntaxError: invalid syntax
l2 = l[:]
l2
[1, 2, 3, 4]
l2 = l2 * 2
l
[1, 2, 3, 4]
l2
[1, 2, 3, 4, 1, 2, 3, 4]
#Para objetos se tiene q llamar a la libreria copy
#import copy
copia_ad = copy.(ad)
SyntaxError: invalid syntax
print(ad)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
import copy
copia_ad = copy.(ad)
SyntaxError: invalid syntax
copia_ad = copy.copy(ad)
print(ad)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
ad.referencia = 1567
print(ad)
Referencia 	1567
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
print(copia_ad)
Referencia 	2034
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
copia_ad.referencia = 1608
print(copia_ad)
Referencia 	1608
Nombre 		Vaso adornado
PVP 		12.0
Descripción 	Vaso de porcelana adornado con árboles
copia_ad
<__main__.Adorno object at 0x0000018961426CB0>
