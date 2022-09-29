import time
#Recursividad
#Dividir un problema en partes mas pequeñas para solucionarlo de forma mas simple

def cuentaatras(num):
    num -=1
    if num > 0:
        print(num)
        time.sleep(1)
        cuentaatras(num)
    else:
        print("BOOOOOOM!!!")
    time.sleep(1)
    print("Fin de la funcion", num)



def factorial(num):
    print("Valor inicial = ", num)
    if num > 1:
        num = num * factorial(num-1)
        time.sleep(1)
    print("Valor final = ", num)
    return num

def sumatorio(numero):
    if numero > 0:
        numero += sumatorio(numero-1)
    return numero
