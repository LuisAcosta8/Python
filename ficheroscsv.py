#ficherosCSV Comma-Separated values
from asyncio import WriteTransport
import csv
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]
#escribir
with open("contactoos.csv","w"), newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
for contacto in contactos:
    writer.writerow(contacto)
#Recuperar informacion
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for contacto in reader:
        print(contacto)
    for nombre, empleo, email in reader:
        print(nombre, empleo)


