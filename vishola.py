from random import randint

x = 0
while x <= 5:
    print(x)
    x = x + 1

else:
    print("El ciclo termino")
    
print(randint(0,100))


def suma(num1,num2):
    total = num1 + num2
    print(total)
suma(5,10)

def func(*args):            #*args Permite trabajar con los argumentos que se le den no es necesario definir un numero en especifico los guarda en tuplas
    return print(sum(args)* 0.05)
func(40,60,760,890)

def fun(**kwargs):          #**kwargs Permite Permite trabajar con los argumentos que se le den no es necesario definir un numero en especifico los guarda en un diccionario
    if "fruit" in kwargs:
        print("Mi fruta escogida es {}".format(kwargs["fruit"]))
    else:
        print("No hay fruta")
fun(fruit="Manzana", veggie="Lechuga")



numeros = [1,2,3,4,5]


#Con FUNCION

def square(numeros):
    result = pow(numeros,2)
    return print(result)

#Con FOR
for item in map(square, numeros):
    print(item)

#Filtrar datos
#Con funcion
def check_even(num):
    return num%2 == 0

#Con for

for n in filter(check_even, numeros):
    print(n)

    #Variables locales vs globales

x = 50 

print("Variable global x: ", x)

def funct(x):
    #global x     Metodo para llamar a la variable global   

    #Reasignacion local
    x = 200
    print("Variable local: ", x)

funct(x)

