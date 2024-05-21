class Cubo:
    
    def __init__(self,ancho,alto,profundo):
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo
        
    def calculo_area(self):
        return self.ancho * self.alto * self.profundo
    
ancho=float(input("Ingrese el ancho: "))
alto=float(input("Ingrese el alto: "))
profundo=float(input("Ingrese la profundidad: "))

# instanciacion 

cubo1=Cubo(ancho, alto, profundo)
print(f"El area del cubo es {cubo1.calculo_area()}")

