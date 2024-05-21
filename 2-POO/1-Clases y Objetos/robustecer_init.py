#  pasar varios argumentos y multiples argumentos
class Persona:
    
    # pueden exiistir em el int tres tipos de argumentos
    # 1. argumentos regulares
    # 2. longitud variable ( va con un *)
    # 3. claves multiples ( clave / valor va con **)
    
    #
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        
        # self en python =this js
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.multiples_valores=valores
        self.clave_valor=terminos
        
    
    def mostrar_persona(self):
        print("Nombre --> ", self.nombre, " Apellido -->  ", self.apellido, " Edad --> ", self.edad)

# ------------------------------------------------------------------------------
# -----------------------cuerpo principal---------------------------------------
# ------------------------------------------------------------------------------


# creacion de objeto
persona1=Persona("Pablo","Alessandrini",36,"racing","talleres",nacionalidad="argentina")
persona2=Persona("Diego","Alessandrini",35,"boca","racing",nacionalidad="peruana")


persona1.mostrar_persona()
persona2.mostrar_persona()

print(f"Valores adicionales {persona1.multiples_valores}")
print(f"Claves adicionales {persona1.clave_valor}")





