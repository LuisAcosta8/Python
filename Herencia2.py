Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: C:/Users/LaPape/Documents/python/Herencia.py ============
ali = Alimento(2015, "Aceite de oliva extra virgen 1t", 5, "1 lt")
print(ali)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(ali)
  File "C:/Users/LaPape/Documents/python/Herencia.py", line 58, in __str__
    Distribuidor \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)
NameError: name 'self' is not defined
+

============= RESTART: C:/Users/LaPape/Documents/python/Herencia.py ============
ali = Alimento(2015, "Aceite de oliva extra virgen 1t", 5, "1 lt")
print(ali)
Referencia 	2015
Nombre 		Aceite de oliva extra virgen 1t
PVP 		5
Descripción 	1 lt
Productor 	
Distribuidor 	
ali.productor = "Aceites Martinez"
ali.distribuidor = "El quevin manchitas"
print(ali)
Referencia 	2015
Nombre 		Aceite de oliva extra virgen 1t
PVP 		5
Descripción 	1 lt
Productor 	Aceites Martinez
Distribuidor 	El quevin manchitas
