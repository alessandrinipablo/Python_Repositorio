# creacion de objetos con argumentos

class Persona:
    
    # vamos a crear objetos con parametros
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
        
# creacion de objeto
# nombre del objeto=clase(parametros)
persona1=Persona("Pablo","Alessandrini",36)
print(persona1.nombre)
print(f"{type(persona1)}")
print(id(persona1))


persona2=Persona("Diego","Alessandrini",35)
print(persona2.nombre)
print(f"{type(persona2)}")
print(id(persona2))

# muestro los nombres de los obejtos del tipo persona