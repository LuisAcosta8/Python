import sys

if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 0 or numero > 9999:
		print("Debes ingresar un numero entre 0 y 9999")
		print("Ejemplo: python Nombredelarchivo.py ####")
	else:
		cadena	= str(numero)
		longitud = len(cadena)
		for i in range(longitud):
			print("{:04d}".format(int(cadena[longitud-1-i])* 10 ** i))
else:
	print("Ejemplo: python Nombredelarchivo.py ####")
