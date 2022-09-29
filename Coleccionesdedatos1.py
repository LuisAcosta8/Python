usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan","Marta"}

administradores.discard("Marta")

print(usuarios)
print(administradores)


administradores.add("Marcos")

print(administradores)


for nombre in usuarios:
    if nombre in administradores:
        print(nombre,"es administrador")
    else:
        print(nombre, "no es administrador")
