#Encapsulacion de atributos y metodos

class Ejemplo:
    __atributoprivado = "Soy un atributo inalcanzable desde fuera"


    def __metodoprivado(self):
        print("Soy un metodo inalcanzable desde fuera")


    def atributo_publico(self):
        return self.__atributoprivado


    def metodo_publico(self):
        return self.__metodoprivado



    
