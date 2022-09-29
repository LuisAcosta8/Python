import random
#random
print(random.random())
#random.uniform (flotante)
print(random.uniform(1, 9))
print(random.uniform(1, 9))
#random.randrange(num1) Devuelve un entero en el rango del numero sino se indica el inicio del rango devuelve un numero entre 0 y menor num1
print(random.randrange(10))
print(random.randrange(0,9))
print(random.randrange(0,101,2)) #Condicionados a los saltos del numero en el tercer argumento
#random.choice()
c = "Hola"
print("Cadena:",c)
print(random.choice(c))
l = [0,1,2,3,4]
print("lista:",l)
print(random.choice(l))
#random.shuffle() #Para listas desordena la lista
print("lista:", l)
random.shuffle(l)
print("Shuffle list:",l)
#random.sample(lista, #elementos)
print("Lista:", l)
print(random.sample(l, 2))
