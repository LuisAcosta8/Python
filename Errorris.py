try:
    n = float(input("Introcude un número: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debes intoducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por 0, prueba otro número")
except Exception as e:
    print(type(e).__name__)
