# creacion de objetos con argumentos

class Persona:
    
    # vamos a crear objetos con parametros
    def __init__(self, nombre, apellido, edad):
        
        # self en python =this js
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    
    def mostrar_persona(self):
        print("Nombre --> ", self.nombre, " Apellido -->  ", self.apellido, " Edad --> ", self.edad)

# ------------------------------------------------------------------------------
# -----------------------cuerpo principal---------------------------------------
# ------------------------------------------------------------------------------


# creacion de objeto
persona1=Persona("Pablo","Alessandrini",36)
persona2=Persona("Diego","Alessandrini",35)
atributos = dir(persona1)
print(f"Atributos antes de agregar uno en el cuerpo principal {atributos}")

# llamo a un metodo --> mostrar persona  de la clase --> persona
# persona1.mostrar_persona()
# aca tengo otra forma, 
# clase.metodo(objeto)
Persona.mostrar_persona(persona1)
persona2.mostrar_persona()

# agregar un atributo en el cuerpo principal no es buena practica igual
persona1.telefono="3586023491"
atributos = dir(persona1)
print(f"Atributos luego de agregar uno {atributos}")



