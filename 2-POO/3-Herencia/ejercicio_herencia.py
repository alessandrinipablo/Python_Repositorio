class Vehiculo(object):
    
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return f"Objeto creado --> [Color : {self.color}, Ruedas: {self.ruedas}]"

# creo la clase vehiculo  
class Coche (Vehiculo):
    
    # constructor con atributos
    def __init__ (self, color, ruedas, velocidad):
        # aclaro los que son heredados
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        
    def __str__(self):
        return f"{super().__str__()}-- > Velocidad {self.velocidad}"
    
    
# creacion de otra clase hija, llamada bicicleta
class Bicicleta(Vehiculo):
    
    # constructor con atributos
    def __init__ (self, color, ruedas,tipo):
        # aclaro los que son heredados
        super().__init__(color, ruedas)
        self.tipo=tipo
    
    # metodo str 
    def __str__(self):
        return f"{super().__str__()}-- >Tipo  {self.tipo}"
        

# creo objeto de clase vehiculo
vehiculo1=Vehiculo("Marron",4)   
print(vehiculo1)


# creo un objeto de la clase hija llamada coche
coche1=Coche("Azul",5,150)
print(coche1)

# creo un objeto de la clase hija biciclete
bici=Bicicleta("Verde",2,"Urbano")
print(bici)