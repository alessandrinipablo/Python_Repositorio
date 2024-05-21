class Aritmetica:
    """
    clase aritmetica para realizar las operaciones de sumar restar etc
    
    """
    # creo el contructor
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    
    # creacion de metodos
    
    def sumar(self):
        # son los atributos de la clase aritmetica
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
# creacion de objetos, y le paso los parametros
aritmetica1=Aritmetica(4,5)

# accedo a los metodos de la clase 
# recordar que como esta dentro de un return
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())

