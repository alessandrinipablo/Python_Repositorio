#metodos del tipo get permiten obtener los atributos de nuestra clase
#metodos del tipo set permite modificar los atributos de nuestra clase

# get --> obtener/ recuperar
# set --> modificar/ cambiar

class Persona:
    def __init__(self, nombre, apellido, edad):
        
        # 1 guion / 2 guiones   da a entender que no se debe modificar, son atributos encapsulados
        # no se debe modificar

        self._nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    # metodo para recuperar el valor del atributo
    # ( garatizo un tratamiento correcto para acceder a los atributos que deben y tienen que ser privados)
    # permite acceder al metodo , cuando se llame como si fuera atributo( no usar el parentesis cuando lo llamo 
    # en el codigo principal)
    @property
    def nombre(self):
        print("Llamado metodo get nombre...")
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print("Llamando metodo set nombre...")
        self._nombre = nombre
    
    
    def mostrar_detalle(self):
        print(f"Persona '{self._nombre}'-' {self.apellido} '-'{self.edad}'")
        
        
# ---------------------------------------------------------------------
# --------------cuerpo principal---------------------------------------
#----------------------------------------------------------------------

# instanciacion
persona1 = Persona("Pablo", "Alessandrini", 36)

# Llamamos al método que me devuelve el valor del atributo oculto
# Al usar el método property no hace falta los paréntesis en el nombre del método
# en conclusion metodo getter
print(f"Obteniendo el atributo de la clase mediante un get: '{persona1.nombre}'")

# @nombre.setter (escribiendo @ el nombre del método.setter, ahora nos permite modificar el nombre
# de manera correcta)

# en conclusion metodo setter
# objeto.metodo
persona1.nombre = "Gabriel"
print(f"Modificando el nombre de manera correcta: '{persona1.nombre}'")

# Mostrar detalles de la persona
persona1.mostrar_detalle()
