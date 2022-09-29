#FOR IN:
#instrucciones
#FIN


arreglo1 = ["Luis", "Kevi", "Emir", "Maria"]
texto = "Ciclo FOR IN"
texto1 = "Con while"
indice = 0

print("\n" +  texto.center(35, "*") + "\n")
for nombre in arreglo1:
    print(nombre)

print("\n" +  texto1.center(35, "*") + "\n")

while indice < len(arreglo1):
    print(arreglo1[indice])
    indice = indice + 1
