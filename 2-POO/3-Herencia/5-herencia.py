# Aca esta el concepto de Herencia, que basica es heredar propiedad de clases 

class Empleado:
    
    # metodo constructor
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido=apellido
        self.edad = edad
        # voy a hacer protegido el salario
        self.__salario = salario
    
    # metodo get para atributos privados
    @property
    def salario(self):
        return self.__salario
    
    #metodos setters para atributos privados, y que tenga una validacion, en este caso entero y positivo
    @salario.setter
    def salario(self, valor):
        if type(valor) == int and valor >=0 :
            self.__salario = valor
        else:
            print("""El salario debe ser un numero entero positivo, 
                  no se permiten valores negativos o invalidos""")
        
        

    
    # metodo que muestra datos.
    def  mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Salario: $", self.salario)
        print("-------------------------------")

#Jefe hereda de Empleado, osea entre parentesis se declara  la clase de la cual va a heredar 
class Jefe(Empleado): 
    # en el contructor se declaran los atributos de la instancia
    def __init__(self, nombre, apellido, edad, salario, departamento_jefatura):
        
        #  atributos que heredan ( super es la palabra clave)
        super().__init__(nombre, apellido, edad, salario)
        
        # atributo propio de esta clase
        self.departamento_jefatura = departamento_jefatura
#  ________________________________________________________________________________________________________________________
# |_________________________________|Cuerpo Principal|_____________________________________________________________________|
# |________________________________________________________________________________________________________________________|


#Ahora vamos a crear una instancia empleado  y una instancia Jefe, y cuando tengo que instanciar, en este caso que Jefe
# hereda de otra clase, siempre se pone la clase hija, y cuando busca los parametros, va a la clase el cual hereda
empleado1 = Empleado("Juan", "Perez",30 ,-5)

Jefe1= Jefe("Luis","Rodriguez",45,-5,"Recursos Humanos")

# como tambien se heredan metodos, cuando quiero mostrar Jefe, uso el metodo de la clase Empleado
empleado1.mostrar_datos()
Jefe1.mostrar_datos()