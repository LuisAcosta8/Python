import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas >9:
        print("Debes introducir un numero entre 0 y 9")
        print("Ejemplo: tabla.py [1-9][1-9]")
    else:
     for f in range(filas):
         print("")
         for c in range(columnas):
             print(" * ", end=' ') #El end indica que no hay salto de linea
else:
    print("Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9][1-9]")
