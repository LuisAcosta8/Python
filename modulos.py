#operaciones
def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r

def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r

def multiplicacion(a,b):
    try:
        r = a * b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r
def division(a,b):
    try:
         r = a / b
    except TypeError:
        print("Error: Tipo de dato no valido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre 0")
    else:
        return r

a, b, c, d = (10, 5, 0, "hola")
print("{} + {} = {}".format(a, b, suma(a,b)))
print("{} - {} = {}".format(b, d, resta(b, d)))
print("{} * {} = {}".format(b, b, multiplicacion(b,b)))
print("{} / {} = {}".format(a, c, division(a,c)))
