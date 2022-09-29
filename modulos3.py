#generador
def leer_numeros(inicio, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error: Número no valido")
        else:
            if valor >= inicio and valor <= fin:
    return valor

def generador():
    numeros = leer_numeros(1, 20, "Cuantos numeros quieres generar? [1-20]")
    modo = leer_numeros(1,3, "[1]Al Alza [2]A la baja [3]Normal")
    lista = []
    for i in range (numeros):
        numero = random.uniform(0,101)
        if modo == 1:
            print("{}  {}".format(numero, math.ceil(numero)))
        elif modo == 2:
            print("{}  {}".format(numero, math.ceil(numero)))
        elif modo == 3:
print("{}  {}".format(numero, math.ceil(numero)))
