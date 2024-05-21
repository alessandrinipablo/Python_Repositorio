# creacion de una clase simple
# tiene que ir la primera letra en mayuscula

"""
# clase sencilla llamada Estableciemientos, que mno tiene nada , solo un pass, para que no haga nada y no de error
class Establecimientos:
    pass

# imprimo y muestro el tipo de elemento creado
print(type(Establecimientos))  

# creacion de objetos a traves de una clase= instanciar
campo1=Establecimientos() 
campo2=Establecimientos() 
campo3=Establecimientos() 
campo4=Establecimientos() 

print(type(campo1))


# forma de instanciar con bucle
lista=[campo1, campo2]
for i in lista:
    i=Establecimientos()
    
"""

""" 
Atributos de clase:
*  Los atributos de clase son variables que se definen dentro de la clase y son compartidas por todas las instancias de esa clase.
   Se definen fuera de cualquier método de la clase, generalmente al principio de la clase.
   Estos atributos son accesibles tanto a nivel de clase como a nivel de instancia.
   Si se modifica el valor de un atributo de clase en una instancia particular, 
   el cambio se reflejará en todas las demás instancias de la clase.
   Se suelen utilizar para almacenar información que es común a todas las instancias de la clase.
"""


"""
* Atributos de instancia:
 Los atributos de instancia son variables que se definen dentro del método __init__() de la clase y son específicas 
 de cada instancia de esa clase.
 
 Se definen utilizando el prefijo self. dentro del método __init__() y están asociados únicamente a la instancia 
 en la que se definen.
 
 Cada instancia de la clase tiene su propio conjunto de valores para los atributos de instancia.
 Estos atributos son accesibles solo a través de la instancia a la que pertenecen.
 Se suelen utilizar para almacenar información única para cada instancia de la clase.

"""
    
# declaracion de la clase establecimientos    
class Establecimiento:
    
    # atributo de clase, porque se define dentro de la clase, pero fuera del init
    # esto significa que todos los objetos creados atraves de la clase Establicimiento, compartiran el atributo provinvcia
    provincia="Buenos aires"
    
    
    #  es un método especial que se llama automáticamente cuando se crea una nueva instancia de una clase. 
    #  Es conocido como el "constructor" de la clase, ya que se utiliza para inicializar los atributos de una nueva instancia.
    #  es donde van los atributos de los objetos creados a partir de una clase
    #  sintaxis ( def __init__ (self, argumentos) )
    # e
    def __init__(self,nombre, localidad, hectareas):
       
        # siempre va self, y el atributo nombre, va a ser igual al argumento nombre
        self.nombre=nombre
        self.localidad=localidad
        self.hectareas=hectareas
    
# creacion del objeto campo1
# cuando le paso los elementos tienen que ser en orden
campo1=Establecimiento("Campo 1","La Puebla",50)
print(type(campo1))
print(campo1.provincia)
print(campo1.nombre)
print(campo1.localidad)
print(campo1.hectareas)
print(type(campo1.nombre))

