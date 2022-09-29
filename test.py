import saludos

saludos.saludar()


from saludos import saludar             #Solo importa la funcion que escribas sespues de import


saludar()


from saludos import *                   #Importa todas las funciones de saludar

#Tambien se pueden importar clases

import saludos

saludos.Saludo()

from saludos import Saludo


#Desde otra carpeta
import sys

sys.path.insert(1, '..')                #.. Buscan en el directorio anterior
print(sys.path)


