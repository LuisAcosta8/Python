titulo1 = "Tareas desordenadas"

tareas = {[6,"Distribucion"],[2,"Diseño"],[1,"Concepción"],[7,"Mantenimiento"],[4,"Producción"],[3,"Planificación"],[5,"Pruebas"]}



print(titulo1.center(80,"*"))
for tarea in tareas:
    print(tarea[0],tarea[1])

from collections import deque

tareas.sort() #Para ordenar
print(tareas) #Para imprimir la lista ordenada


#[]
#{}
    
