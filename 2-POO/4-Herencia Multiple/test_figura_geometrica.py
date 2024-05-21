from Cuadrado import Cuadrado 
from rectangulo import Rectangulo

# instancio 
# paso los atributos que necesito ancho, lado, y color

print("Creacion del Objeto Rojo - Cuadrado ".center(50,"-"))
cuadrado1= Cuadrado(5, 5, "Rojo")
print(f"El area del cuadrado es {cuadrado1.calcular_area()}")
print(cuadrado1)
# muestro por pantalla como puedo acceder a los metodos de la clase cuadrado( y como actuan los metodos heredables)
"""
# atributo
print(f"Ancho --> {cuadrado1.ancho}")
# atributo
print(f"Alto --> {cuadrado1.alto}")
# metodo
print(f"Metodo calcular area --> '{cuadrado1.calcular_area()}'")
# atributo
print(f"Color --> {cuadrado1.color}")
"""

# Importancia de como se van a llamar los metodos 

# MRO Method Resolutions Order (Permite resolver metodos de Jerarquias de Clases)
# el mismom devuelva la imformacion de en que orden se van a ejecutar los metodos, segun la jerarquia de clases 
# que definimos.
"""
orden=Cuadrado.mro()
print(orden)
"""
"""
cuadrado2=Cuadrado(10,10,"Verde")
print(f" El area es {cuadrado2.calcular_area()}")
print(cuadrado2)

"""
print("Creacion del Objeto Rectangulo -Anaranjado ".center(50,"-"))
# instanciamos
# otra forma 
rectangulo1=Rectangulo(ancho=5,alto=8,color="anaranjado")

# ejecutamos un metodo 
print(f"El area del rectangulo es:{rectangulo1.calcular_area()}")

# mostramoos el objeto
print(rectangulo1)


