# Encapsular todos los atributos de una clase
# y agrego metodo destructor tambien
class Persona:
    # encapsulo la clase completa
    def __init__(self, nombre, apellido, edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido 
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido 
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad       
    
    def mostrar_detalle(self):
        print(f"Persona '{self._nombre}'-' {self._apellido} '-'{self._edad}'")

    # metodo dunder que permite la eliminacion de objetos
    def __del__(self):
         print("Se procede a eliminar el objeto.... ")
         print(f"\tPersona '{self._nombre}'-' {self._apellido} '-'{self._edad}'")
# ---------------------------------------------------------------------
# --------------cuerpo principal---------------------------------------
#----------------------------------------------------------------------

if __name__ == "__main__":
    print("Estamos dentro del archivo, que tiene la clase persona, se procede a ejecutar.....")
    # instanciacion
    persona1 = Persona("Pablo", "Alessandrini", 36)
    # objeto creado 
    persona1.mostrar_detalle()

    # acceder a los archivos mediantes getters and setters

    # cambio atributo nombre
    persona1.nombre = "Diego"
    print(f"Modificando el nombre de manera correcta: '{persona1.nombre}'")

    # cambio atributo apellido
    persona1.apellido = "Gonzalez"
    print(f"Modificando el apellido de manera correcta: '{persona1.apellido}'")

    # cambio atributo edad
    persona1.edad=38
    print(f"Modificando la edad de manera correcta: '{persona1.edad}'")

    # Mostrar detalles del objeto con los datos actualizados
    persona1.mostrar_detalle()

    print(__name__)
