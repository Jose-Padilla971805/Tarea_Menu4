import os

def ejercicio3():
        class Banco:

            def __init__(self):
                self.cliente1=Cliente("jose")
                self.cliente2=Cliente("pablo")
                self.cliente3=Cliente("luis")

            def operacion(self):
                self.cliente1.depositar(1500000)
                self.cliente2.depositar(78000)
                self.cliente3.depositar(53000)
                self.cliente1.extraer(65000)

            def depositos(self):
                total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
                print("El total de dinero del banco es: ",total)
                self.cliente1.imprimir()
                self.cliente2.imprimir()
                self.cliente3.imprimir()


        class Cliente:

            def __init__(self,nombre):
                self.nombre=nombre
                self.cantidad=0


            def depositar(self,cantidad):
                self.cantidad+=cantidad

   
            def extraer(self,cantidad):
                self.cantidad-=cantidad

          
            def devolver_cantidad(self):
                return self.cantidad

      
            def imprimir(self):
                print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)



        banco1=Banco()
        banco1.operacion()
        banco1.depositos()