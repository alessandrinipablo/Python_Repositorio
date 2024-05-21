# creacion de clases  recordar que siempre van en mayuscula
# normalmente siempre se trabaja con los objetos ( creacion ) y no con la clase (entidad)



# una clase puede tener atributos y metodos

# atributos = cualidades
# metodos = acciones
class Persona:
    
    atributo_de_clase ="Hola soy atributo de clase (estoy antes del inicializador)"
    # metodo inicializador 
    # parametro por default que si o si se tiene que pasar
    # cuando tiene doble guion bajo son los metodos dunder
    
    def __init__(self):
        # al no tener parametros, los parametros serian como constantes, todos los objetos que cre se van a llaamar igual
        self.nombre="Pablo"
        self.apellido="Alessandrini"
        self.edad=36
        


# corroborar el tipo de dato que cree

tipo=type(Persona)
print(f"El tipo de dato que se creo es {tipo}")

# creacion de objeto o instanciacion
# pongo el objeto que voy a crear y lo igualo al nombre de la clase
persona1=Persona()
# mostrar los datos del objeto
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)