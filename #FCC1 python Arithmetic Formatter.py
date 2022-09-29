#FCC1 python Arithmetic Formatter

#def arithmetic_arranger(list, bool):

lista = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
lista2 = []
for i in lista:
    a = i.split(" ")
    lista2.append(a)

print(lista2)

print(lista2[0][0]+"\t",lista2[1][0]+"\t",lista2[2][0]+"\t",lista2[3][0]+"\t")

    