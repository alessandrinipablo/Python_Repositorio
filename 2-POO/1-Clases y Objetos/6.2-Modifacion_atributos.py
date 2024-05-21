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
print(f"Nombre del Objeto 1 {persona1.nombre}, apellido: {persona1.apellido} y edad {persona1.edad}")
#print(f"{type(persona1)}")
#print(id(persona1))


persona2=Persona("Diego","Alessandrini",35)
print(f"Nombre del Objeto 2 {persona2.nombre}, apellido: {persona2.apellido} y edad {persona2.edad}")
#print(persona2.nombre)
#print(f"{type(persona2)}")
#print(id(persona2))

# modificar atributos del objeto creado
persona1.nombre="Gabriel"
persona1.apellido="Rodriguez"
persona1.edad=37
print("Mostrar los cambios del objeto 1")
print(f"Nombre del Objeto 1 {persona1.nombre}, apellido: {persona1.apellido} y edad {persona1.edad}")