
# Los getters se utilizan para obtener valores de atributos privados. 
# los setters se utilizan para establecer nuevos valores, con la posibilidad de realizar validaciones adicionales.

# creacion de clase empleeado
class Empleado:
    
    # creacion de atributos
    def __init__(self, nombre, apellido, edad, salario,horas_extras):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # guion bajo al principio  significa que el atributo es privado, se puede modificar fuera de la clase
        # pero no es recomendado
        self.__salario = salario
        
        self.__horas_extras=horas_extras
    
    # obtener los getters
    @property
    def horas_extras(self):
        return self.__horas_extras
    
    
    @horas_extras.setter
    def horas_extras(self, horas_extras):
        # valido el parametro que luego voy a cambiar en el cuerpo, para efectivamente hacer el cambio o no
        if (horas_extras>=0) :
            self.__horas_extras=horas_extras
        else:
            print("No se pueden realizar cambios en las horas extras")   

    
    """
    Forma estilo Java
    # forma de obtener  un valor del atributo privado
    def get_horas_extras(self):
        return self.__horas_extras

    # forma de poder modificar un atributo privado   
    # es recomendable hacer algun tipo de verificacion a la hora del seteo. 
    def set_horas_extras(self, horas_extras):
         
         # valido el parametro que luego voy a cambiar en el cuerpo, para efectivamente hacer el cambio o no
         if (horas_extras>0) :
             self.__horas_extras=horas_extras
         else:
            print("No se pueden realizar cambios en las horas extras")
     """
 
 
    def sueldo(self):
        #Metodo que devuelve el sueldo total del trabajadors
        print(f"El empleado {self.nombre} {self.apellido} gana ${self.__salario} y tiene {self.__horas_extras} HE")

#=====================================================================================================================
# =========================CUERPO PRINCIPAL===========================================================================
#=====================================================================================================================



# Crear una instancia de Empleado
empleado1 = Empleado("Juan", "Pérez", 30, 30000,45)
empleado2 = Empleado("Pablo", "Alessandrini", 30, 30000,45)
empleado3 = Empleado("Juan", "Pérez Garcia", 30, 30000,45)


# Acceder a los atributos de la instancia
print("Nombre:", empleado1.nombre)
print("Apellido:", empleado1.apellido)
print("Edad:", empleado1.edad)
# comento esta linea porque para acceder, una vez declarado los atributos como privados o protegidos, 
# me da error si los accedo de la siguiente manera, por eso hay que aplicar los getters y setters en ese orden
#print("Salario:", empleado1.__salario)
#print("Horas extras:", empleado1.__horas_extras)

# llamo a la instancia con un metodo
# empleado1.sueldo()

# aplicado correctamente los getters y setters

# antes del cambio
# metodo estilo java
# empleado1.get_horas_extras()
# empleado1.horas_extras(-9)

# APLICADO LOS METODOS DE PYTHON 
# si quiero modificar el atribuo protegido, asi se hace ( recordar que siempre se tienen que hacer estos pasos-->
# poner doble guion bajo donde quiero proteger los atributos
# a la funcion get, dela atributo que quiero trabajar, se pone @property y el nombre de la funcion tiene que ser por 
# nomrbe el mismo nombre del atributo, y retorna el mismo
# en la funcion set, va a @ y el nombre de la funcion que puse property, y para setear se llama a la funcion que es setters
empleado1.horas_extras=0
empleado1.sueldo()