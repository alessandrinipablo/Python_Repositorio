from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    
    # inicializador
    def __init__(self, ancho,alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    
    # metodo que calcula el area   
    def calcular_area(self):
        return self.ancho*self.alto
    
    # metodo string 
    def __str__(self):
        return f" {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"

    