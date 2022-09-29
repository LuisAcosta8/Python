titulo1 = "Estadisticas originales"
titulo2 = "Estadisticas balanceadas"

caballero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
guerrero  = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero   = {"vida":2,"ataque":2,"defensa":2,"alcance":2}


print(titulo1.center(80,"*"))
print("Caballero: ", caballero)
print("Guerrero: ", guerrero)
print("Arquero: ", arquero)

caballero["vida"] = guerrero["vida"]*2
caballero["defensa"] = guerrero["defensa"]*2
guerrero["ataque"] = caballero["ataque"]*2
guerrero["alcance"] = caballero["alcance"]*2
arquero["vida"] = guerrero["defensa"]
arquero["ataque"] = guerrero["ataque"]
arquero["defensa"] = guerrero["defensa"]/2
arquero["alcance"] = guerrero["alcance"]*2


print(titulo2.center(80,"*"))
print("Caballero: \t", caballero)
print("Guerrero: \t", guerrero)
print("Arquero: \t", arquero)
