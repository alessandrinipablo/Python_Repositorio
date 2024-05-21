# creacion de la clase
class Rectangulo:
    
    # inicializador
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    # metodos    
    def area(self):
        return self.base * self.altura
    
# pedir por usuario
base=int(input("Ingrese la base del rectangulo: "))   
altura=int(input("Ingrese la altura del rectangulo:")) 

# instanciar
rectangulo1=Rectangulo(base, altura)

# aplicar metodo
print("El area del rectangulo es: ",rectangulo1.area())
