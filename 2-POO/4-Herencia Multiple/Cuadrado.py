# importamos las clases padres
from FiguraGeometrica import FiguraGeometrica
from Color import Color


# creamos la clase hija que hereda de dos clases padres
class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, alto, ancho, color):
        #super().__init__(lado, color) no es recomendable, usar, cuando se heredan de dos padres
        # se  hace asi, nombre de clase.inicializador, y los metodos que hereda
        
        # hereda el los atributos de figura geometrica
        FiguraGeometrica.__init__(self,ancho, alto)
        # hereda color
        Color.__init__(self, color)
        
    
    
    # metodo calcular area  
    def calcular_area(self):
        return self.ancho * self.alto 
    
    def __str__(self):
        # heredo los metodos str de ambas clases padres
        return f" {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"