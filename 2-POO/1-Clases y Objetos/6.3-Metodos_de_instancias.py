# creacion de objetos con argumentos

class Persona:
    
    # vamos a crear objetos con parametros
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    # metodos de clase  
    # crear un metodo que recibe el parametro self, para poder nombrar los atributos, cuando 
    # se crea un objeto,y lo invocamos en el codigo principal
    def mostrar_persona(self):
        print("Nombre --> ", self.nombre, " Apellido -->  ", self.apellido, " Edad --> ", self.edad)
        

persona1=Persona("Pablo","Alessandrini",36)
# forma vieja
print(f"Nombre del Objeto 1 {persona1.nombre}, apellido: {persona1.apellido} y edad {persona1.edad}")
# llaman al metodo
persona1.mostrar_persona()



persona2=Persona("Diego","Alessandrini",35)
print(f"Nombre del Objeto 2 {persona2.nombre}, apellido: {persona2.apellido} y edad {persona2.edad}")
persona2.mostrar_persona()

