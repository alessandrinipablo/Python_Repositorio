# destructores de objetos
# para eliminar m

from encapsulando_total import Persona


print("Creacion de objetos".center(50,"-"))
persona1=Persona("Lionel","Messi",36)
persona1.mostrar_detalle()


print("Eliminacion de objetos".center(50,"-"))
# llamamos al metodo del que me permite eliminar un objeto
# es poco comun pero se puede usar el metodo del
del persona1