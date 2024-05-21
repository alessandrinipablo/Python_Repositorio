class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def __str__ (self):
        return f"El nombre del animal es {self.nombre}"
    
    def moverse(self):
        print("El animal se mueve")
        
class Perro(Animal):
    
    def moverse(self):
        print(f"El {self.nombre} camina")
        
class Pez(Animal):
    
    def moverse(self):
        print(f"El  {self.nombre} nada")

class Reptil (Animal):
    
    def moverse(self):
        print(f"El  {self.nombre} se desplaza")

# metod que recibe una variable, y luego esa variable ,que seria el objeto una vez creado, se usa para llamar 
# a los metodos de la clase animal, que va a trabajar segur el tipo de aninal ( clase hija) que sea
def trabajaAnimal (animal):
    print(animal)
    animal.moverse()

print("Elija una opcion\n1-Perro\n2-Pez\n3-Reptil") 
opcion=int(input("Opcion: "))
nombre=input("Que nombre tiene: ")

if opcion == 1:
    mascota=Perro(nombre)
elif opcion == 2:
    mascota=Pez(nombre)
else:
    mascota=Reptil(nombre)
 
trabajaAnimal(mascota)