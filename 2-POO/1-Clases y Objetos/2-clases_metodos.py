class Establecimiento:
    
    def __init__ ( self, nombre, localidad, hectareas):
        self.nombre = nombre 
        self.localidad= localidad
        self.hectareas = hectareas
    
    #Metodos    
    def nombre_campo(self):
        # usando la palabra self, accedemos a nuestros propios valores, o sea los atributos
        print(f"El nombre del campo es {self.nombre}")
        
    def  mostrar_localidad(self):
        print(f"La ciudad donde se encuentra el campo {self.nombre}   es {self.localidad}")
        
    def cantidad_hectareas(self):
        print(f"El campo tiene {self.hectareas}")

# creo el objeto
campo1 = Establecimiento("La Puebla","Arias", 50)
campo2 = Establecimiento("Las Marias","Arias", 60)
campo3 = Establecimiento("Las Rosas","Arias", 70)
campo4 = Establecimiento("La Aurora", "Alejo Ledesma", 20)


# llamando a los metodos
campo1.mostrar_localidad()
campo2.mostrar_localidad()


campos=[campo1,campo2,campo3,campo4]
# uso un bucle for para recorrer
for i in campos:
    print(f"Nombre: {i.nombre}")
    print(f"Localidad: {i.localidad}")
    print(f"Cantidad de hectareas: {i.hectareas}")
    print("--------------------")
    
    
