import os

def ejercicio1():
    class Alumno:
        
        def inicializar(self):
            self.nombre = input("digite nombre => ")
            self.nota = float(input("digite su nota => "))

        
        def imprimir(self):
            print("Nombre: ",self.nombre)
            print("Nota: ",self.nota)

        
        def resultado(self):
            if self.nota >= 3:
                print("El alumno aprobo")
            else:
                print("El alumno no aprobado")
    

    alumno1=Alumno()
    alumno2=Alumno()
    alumno1.inicializar()
    alumno1.imprimir()
    alumno1.resultado()
    alumno2.inicializar()
    alumno2.imprimir()
    alumno2.resultado()