titulo1 = "Si el usuario ingresa letras en lugar de numeros"
titulo2 = "Método try: "
titulo3 = "Try con while"
titulo4 = "Finally"
titulo5 = "None"
#Errores


print(titulo1.center(80,"*"))
n = float(input("Introduce un numero: "))
m = 10
print(" {} * {} = {}".format(n,m,n/m))


print(titulo2.center(80,"*"))
try:
    x = float(input("Introduce un numero: "))
    y = 10
    print(" {} * {} = {}".format(x,y,x/y))
except:
    print("Ha ocurrido un error, Introduce un numero: ")


print(titulo3.center(80,"*"))
while(True):
    try:
        x = float(input("Introduce un numero: "))
        y = 10
        print(" {} * {} = {}".format(x,y,x/y))
    except:
        print("Ha ocurrido un error, Introduce un numero: ")

    else:
        print("Todo ha funcionado correctamente")
        break       #Se debe romper el while para que no se haga un ciclo infinito


print(titulo4.center(80,"*"))
while(True):
    try:
        x = float(input("Introduce un numero: "))
        y = 10
        print(" {} * {} = {}".format(x,y,x/y))
    except:
        print("Ha ocurrido un error, Introduce un numero: ")

    else:
        print("Todo ha funcionado correctamente")
        break       #Se debe romper el while para que no se haga un ciclo infinito
    finally:
        print("Fin de la iteración")


print(titulo5.center(80,"*"))
def dividir(a, b):
    if b == 0:
       return None
    return a/b
