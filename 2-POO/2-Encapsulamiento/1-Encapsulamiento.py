class Picachu:
    
    # atributo de clase, porque esta dentro de la clase, pero fuera del contructor, osea, todos los objetos, que 
    # se creen con esta clase heredan  el atributo
    tipo="electrico"
    
    # constructor
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre=nombre
        self.nivel=nivel
        self.salud=salud
        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max
        self.__color=color
    
    # declaracion de un metodo llamado atacar    
    def atacar(self):
        print(f"Picachu llamado {self.nombre} ataca y genera {self.nivel/4} de daño")

# creacion de objetos

picachu1=Picachu("Pablo",780,100,6,2,"Amarillo")
picachu2=Picachu("Pablo1",780,100,6,2,"Amarillo")
picachu3=Picachu("Pablo2",780,100,6,2,"Amarillo")
picachu4=Picachu("Pablo3",780,100,6,2,"Amarillo")
picachu5=Picachu("Pablo4",780,100,6,2,"Amarillo")
picachu6=Picachu("Pablo5",780,100,6,2,"Amarillo")
# creo una lista con los nombres de los atributos de clase Picachu
atributos_picachu=["nombre","nivel", "salud","voltaje_max","amperaje_max","color"]
# creo una lista con los objetos creados
picachus_creados=[picachu1,picachu2,picachu2,picachu4,picachu5,picachu6]

# Recorrer la lista de instancias de Picachu
# primero recorro la lista de los picachus creados
for picachu in picachus_creados:
    print(f"Nombre del Picachu: {picachu.nombre}")
    
    # Luego Recorrer la lista de nombres de atributos y obtener los valores
    for atributo in atributos_picachu:
        # guardo en una variable  llamada 'valor atributo'  y le paso una funcion que deber recibir, el nombre del objeto, y el atributo
        valor_atributo = getattr(picachu, atributo)
        # muestro atributo y valor
        print(f"{atributo}: {valor_atributo}")
    print("--------------------------------")


# quiero cambiar un valor, ejemplo el nombre
print(f"Nombre viejo {picachu1.nombre}")
picachu1.nombre="Jesus"
print(f"Nombre nuevo {picachu1.nombre}")

# accediendo a metodos
# picachu3.atacar()

# puede haber dos tipos variables, o en este caso atributos 
# publicos y privados, la diferencia radica que los atributos publicos, se pueden acceder de cualquier lado, y pueden der modificados
# y los privados solo son accesibles desde la clase.abs
# Entonces ahi entra en juego algo muy importante que el encapsulamiento.
# en python se soluciona con lineas de codigo.

class Alumno:
    def __init__(self,nombre,edad):
        # dos guiones bajos es para atributo privado
        self.__nombre=nombre 
        # un guion bao es atributo protegido
        self._edad=edad
        
    def mostrar_datos(self):
        return f"El alumno {self.__nombre} tiene {self._edad} años."
    
print("----")
alumno1=Alumno("David",17)
print(alumno1.mostrar_datos())

print("Vamos a modificar....")
alumno1.__nombre="PABLO"
alumno1._edad=37
# aca me da error cuando quiero mostrar unatributo protegido
print(alumno1.__nombre)


# metodos publicos o privados
# publico se puede modificar en cualquier lado, y privados solo en la clase. 
