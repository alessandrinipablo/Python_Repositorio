# sobreescritura del metodo __str__
""" 
El método __str__ en Python:

Se utiliza para definir una representación legible y amigable de un objeto.
Es invocado por print() y str().
Debe devolver una cadena (str) que describe al objeto de manera comprensible.
Definir __str__ en tus clases hace que tus objetos sean más fáciles de entender y depurar, 
especialmente cuando se imprimen o se convierten en cadenas.

"""
# vamos a importa la clase persona y empleado del arhivo herencia ( para crear personas y empleados)
from herencia import *


# instanciacion de la clase persona
persona1=Persona("Cesar","36")
# imprimo los datos del objeto usando el metodo __str__
print(persona1)


# instanciacion de la clase empleado ( que heredea de la clase persona)

empleado1=Empleado("Diego",35,750000)

# si mando a imprimir, como tambien hereda el metodo str, aunque como el metodo esta en la clase padre, no 
# va a poder heredar el atributo que esta en la clase hija en este caso el sueldo, para eso hay que crear el 
# str en la clase hija

print(empleado1)
