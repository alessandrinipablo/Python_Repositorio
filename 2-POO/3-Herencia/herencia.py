# si bien de manera implicita, esta clase es la padre, para quedarnos seguros, le ponemos clase objects, y nos
# garantizamos que lo sea
class Persona(object):
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # metodo dunder str 
    # para luego llamando al obejto creado mediante prin, usa este metodo
    # basicamente sirve para mostrar por pantalla los datos del objeto
    def __str__(self):
        return f"Persona [Nombre: '{self.nombre}', Edad: '{self.edad}']"
        
        
#creacion de la clase hija, llamada Empleado, hereda de la clase Persona        
class Empleado(Persona):
    # la clase hija se declara un init, o constructor
    # tambien se le deben pasar los atributos, ( los propios de la clase, y los que heredaria de otra)
    # abajo se tiene que poner super().__init__ y van los atributos que hereda de otra clase, en este caso Persona
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def __str__(self):
        # aca tambien aplicamos el concepto de herencia, en el return ponemos super y el metodo que queremos herededar
        return f"{super().__str__()} --> [Sueldo: {self.sueldo}]"
        
if __name__=="__main__":
            
    # instanciacion

    empleado1=Empleado("Pablo",36,730000)

    # accedo al atributo nombre

    # accediendo a la clase hija , con atributos de la clase padre
    print(empleado1.nombre)

    # accediendo a la clase hija con atributos propios
    print(empleado1.sueldo)