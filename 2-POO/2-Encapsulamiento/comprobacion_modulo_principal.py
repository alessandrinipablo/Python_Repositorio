# usando modulos  y clases

from encapsulando_total import Persona

# otra forma que solo ejecute lo que yo quiero 
if __name__=="__main__":
    persona1=Persona("Lionel","Messi",36)

    persona1.mostrar_detalle()

# propiedad dunder name  
#print(__name__)

"""
usando la palabra name me sirve para saber donde estoy trabajando ( cuando trabajo con importaciones)
si estoy trabajando en el archivo donde uso las importaciones, me devuelve  en nombre del archivo que importo sin .py
y  la palabra __main 

si a eso lo mismo lo hago desde el archivo original, solo me devuelve __main__
"""