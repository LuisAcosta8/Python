class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de residencia:", self.residencia)

class Empleado(Persona):
    def __init__(self, nombre, edad, residencia, salario, antiguedad):

        #Valores fijos se tiene que modificar el super para poder ingresarlo desde teclado 
        # super().__init__("Antonio Cuenca", 29, "CDMX")
        super().__init__(nombre, edad, residencia)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario, "\nAntigüedad:", self.antiguedad, "años")

    
Antonio = Empleado("Antonio", 29,"Puerto Rico",1500,15)
print(Antonio.nombre)
print(Antonio.edad)
print(Antonio.residencia)
print(Antonio.salario)
print(Antonio.antiguedad)
Antonio.descripcion()


#PRINCIPIO DE SUSTITUCION aplicar terminos 'es siempre in o una'(un objeto de la sub es un objeto de la super)

#isinstance() True or False

print(isinstance(Antonio,Empleado))
print(isinstance(Antonio,Persona))

