#Herencia multiple
#Solo en python
#Posibilidad que una sub clase herede de varias clases a la vez
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este metodo lo heredo de A")
        

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este metodo lo heredo de B")
        

class C(A,B):
    def c(self):
        print("Este metodo es único de c")

#c = C()
#Le da prioridad a la que se encuentra a la izquierda
#class C(A,B): da prioridad a A
#class C(B,A): da prioridad a B
#c.a()
#c.b()
#c.c()
