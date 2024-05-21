class Productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre=nombre
        # un guion bajo significa que es oculto el valor, y que no se deberia acceder en el cuerpo principal 
        # solo ser accesible dentro de la misma clase
        self._precio=precio
        
        # acceso restringido
        self.__cantidad=cantidad
        
        
        def mostrar (self):
            print("Nombre: ", self.nombre)
            print("Precio: ", self.precio)
            print("Cantidad: ", self.cantidad)
            
producto1=Productos("Notebooks",1230,10)
producto1=Productos("Celular",1000,100)
producto1=Productos("Parlante",130,180)
producto1=Productos("Pc",1350,1630)