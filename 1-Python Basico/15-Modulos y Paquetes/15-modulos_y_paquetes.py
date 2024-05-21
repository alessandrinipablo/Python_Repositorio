""" Módulos: Archivos individuales que contienen código Python reutilizable.
    Paquetes: Colecciones de módulos organizados en una estructura de directorios.
    Scripts: Archivos de texto plano que contienen una secuencia de instrucciones Python y pueden ser ejecutados directamente.
"""

# una forma de importar

import modulos_importables

# llamo a la funcion sumar del modulo modulos_importables
print(modulos_importables.sumar(2,3))
print(modulos_importables.restar(2,3))
print(modulos_importables.multiplicar(2,3))
print(modulos_importables.dividir(2,3))  

# otra forma es la siguiente 
# de modulos_importables  importame solo sumar, para que solo con la palabra sumar alcance
from  modulos_importables import sumar, nombre_autor

print(f"Aca aplico solo llamando a la funcion suma {sumar(4,5)}")

# aca le estoy diciendo, de modulos_importables importame todo(no es recomendable)
# from  modulos_importables import *

# importando solo un valor
print(nombre_autor)


# importar un paquete 
# le tengo que poner, desde (nombre del paquete) tomar el scprit ( llamado funciones) importar la parte que quiero 
from paquete.funciones import factorial

# muestro la funcion 
print(f"Calcular factorial {factorial(8)}")

# otra forma de importar , solo digo que quiero importar el paquete y el archivo
import paquete.funciones
# va el paquete, luego el script, luego la funcion
print(paquete.funciones.factorial(8))

# aca importo tambien otra cosa del paquete

print(paquete.funciones.nombre_autor)

# importar usando alias
# digo que voy a importar del paquete, el script y lo renombro
import paquete.funciones as funciones

print(f"Uso la importacion pero usando alias \n{funciones.factorial(9)} ")

# importacion de subpaquetes
import paquete.sub_paquete.sub_funciones as contarletras
nombre="Pablo Gabriel Alessandrini"

# me va a contar la cantidad de letras sin contar los espacios
print(contarletras.contar_letras("Hola como estas"))
print(contarletras.contar_letras(nombre))

