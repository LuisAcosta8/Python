from io import open
documento = open("BD.txt","r")
line = documento.readlines()
print(line)
documento.close()