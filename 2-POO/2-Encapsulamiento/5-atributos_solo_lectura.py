# cuando no quiero que se modifique el valor de un atributo

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
    
##metodos del tipo get permiten obtener los atributos de nuestra clase
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

    @property
    def nombre(self):
        print("Llamado metodo get nombre...")
        return self._nombre
    
    #@nombre.setter
    #def nombre(self, nombre):
    #    print("Llamando metodo set nombre...")
    #    self._nombre = nombre
    
    
    def mostrar_detalle(self):
        print(f"Persona '{self._nombre}'-' {self.apellido} '-'{self.edad}'")
        
        
# ---------------------------------------------------------------------
# --------------cuerpo principal---------------------------------------
#----------------------------------------------------------------------

# instanciacion
persona1 = Persona("Pablo", "Alessandrini", 36)


print(f"Obteniendo el atributo de la clase mediante un get: '{persona1.nombre}'")

persona1.nombre = "Gabriel"
print(f"Modificando el nombre de manera correcta: '{persona1.nombre}'")

persona1.mostrar_detalle()

"""  
Al quitar el metodo setter me va a dar un error
Debdio a que no podemos modificar el valor de ese atributo.
Son variables de solo lecturoa

"""
    
    