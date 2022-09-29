from io import open
documento = open("personas.txt", "r")
campos = ["ID", "Nombre", "Apellido", "Fecha de nacimiento"]
lista = []
for line in documento:
    line = line.replace("\n", "")
    line = line.split(";")
    dic = {campos:line for (campos,line) in zip(campos,line)}
    lista.append(dic)
for it in lista:
    print("{}) {} {} años, nacio el {}".format(it["ID"], it["Nombre"], it["Apellido"], it["Fecha de nacimiento"]))
