# La clase abstracta (o clase padre en este contexto) define la estructura o forma de trabajo mediante métodos 
# abstractos que deben ser implementados por cualquier clase que herede de ella.
# .Las clases hijas (subclases) son las que pueden ser instanciadas y deben cumplir con la estructura definida por la clase 
"""
Clase Padre (Clase Abstracta):
    Define la estructura y los métodos abstractos que deben ser implementados por las clases hijas.
    No puede ser instanciada directamente.
    Actúa como una plantilla o contrato que asegura que las subclases implementen ciertos métodos.

Clases Hijas (Subclases):
    Heredan de la clase abstracta.
    Deben implementar todos los métodos abstractos definidos en la clase abstracta.
    Pueden ser instanciadas y utilizadas para crear objetos concretos.

"""

from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # metodo abstracto que si o si en la creacion de clases hijas tengo que crear
    @abstractmethod
    def descripcion(self):
        pass

# Clase hija que hereda de Animal
class Perro(Animal):
    
    # metodo que obligadamente tengo que usar
    def descripcion(self):
        return f"Perro: {self.nombre}, hace 'Guau'"

# Otra clase hija que hereda de Animal
class Gato(Animal):
    
    def descripcion(self):
        return f"Gato: {self.nombre}, hace 'Miau'"

# Instanciación de las clases hijas
perro = Perro("Firulais")
gato = Gato("Michi")

# Uso de los métodos implementados
print(perro.descripcion())  
print(gato.descripcion())   