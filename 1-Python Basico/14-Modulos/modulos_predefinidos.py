# Documentación del módulo os: https://docs.python.org/es/3/library/os.html

# Documentación del módulo sys: https://docs.python.org/es/3/library/sys.html

# Documentación del módulo platform: https://docs.python.org/es/3/library/platform.html


# SYS -->  acceso a algunas variables y funciones relacionadas con el intérprete de Python
import  sys 

# os --> proporciona funciones para interactuar con el sistema operativo subyacente
import os 


# platform --> proporciona información sobre la plataforma en la que se está ejecutando Python
import platform as pl

funciones_os=dir(os)
funciones_sys=dir(sys)
funciones_platform=dir(pl)

#print(funciones_os)
#print(funciones_sys)
#print(funciones_platform)

# muestra donde esta instalado el modulo 
print(os.path)

print(os.name)

print(sys.platform)

# devuelve la direccion del archivo/script donde esta actualmente
# get current directory working ( ruta absoluta)
print(os.getcwd())  

# cambio el directorio
os.chdir("..")

# verifico que cambio el directorio.
print(os.getcwd())

# cambio el directorio de vuelta
os.chdir("..")

# muestro la lista de files que estan el el directorio
print(os.listdir())

# este es lo mismo 
print(os.listdir(os.getcwd()))

# crear un directorio, en este caso me cambio donde quiero crear las carpetas
os.chdir("..")

# verifico que cambio el directorio.
print(os.getcwd())

# creo el nombre del directorio que quiero  crear, lo pongo comentado para que no se ejecute de vuelta para que no de error
#os.mkdir("Progrmacion Orientada a Objetos")
#os.mkdir("Python Basico")
#os.mkdir("Lista Temas")

#os.path.join(): Esta función se utiliza para unir componentes de ruta en una sola ruta. 

print(os.listdir()) # muestra los ficheros y carpetas que hay dentro de PYTHON
ruta_completa=os.path.join("PYTHON","Python Basico","archivo_prueba.txt")
print(f"Creacion de la ruta {ruta_completa}")

#os.path.exists(): Esta función se utiliza para verificar si un archivo o directorio existe en la ruta especificada.
if os.path.exists("A-python_basico.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe puede crearlo")


# os.path.basename(): Esta función se utiliza para obtener el nombre base de un archivo o directorio de una ruta.
ruta ='C:\\Users\\Usuario\\Desktop\\Python\\Python Basico'
nombre_file=os.path.basename(ruta)
print(f"El nombre de {nombre_file}")


# os.path.abspath
#print(os.getcwd())
print(os.listdir(os.getcwd()))
nombre_archivo="11-exepciones.py"
ruta_absoluta = os.path.abspath(nombre_archivo)
print(f"La ruta absolulta del archio {nombre_archivo} es \n{ruta_absoluta}\n")


# os.path.dirname(): Esta función se utiliza para obtener el nombre del directorio de una ruta.
ruta2='C:\\Users\\Usuario\\Desktop\\Python\\Python Basico'
directorio=os.path.dirname(ruta2)
print(f"El directorio es {directorio}")

#os.path.splitext(): Esta función se utiliza para dividir una ruta en la parte base del nombre del archivo y su extensión.
ruta = "/ruta/a/mi/archivo.txt"
nombre, extension = os.path.splitext(ruta)
print("Nombre:", nombre)
print("Extensión:", extension)

print("Saliendo")
# sale del programa
# sys.exit()
# print("Esta linea no deberia moestrarse")

# version del sistema operativo
print(sys.getwindowsversion())

# modulos cargados por python
#print(sys.modules)

# version de python
print(sys.version)
print(sys.version_info)


# metodos de platform
# arquitectura del sistema operativo, es decir, si es de 32 bits o 64 bits.
print(pl.architecture())

# arquitectura de la máquina, como "x86", "x86_64", "AMD64", etc.
print(pl.machine())

# Devuelve una cadena que describe el procesador del sistema, com
# "Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz", "AMD Ryzen 7 3700X 8-Core Processor", 
print(pl.processor())

# proporciona información sobre la plataforma del sistema operativo, como el sistema operativo en sí y la versión del kernel
print(pl.platform())

#Devuelve una cadena que indica el nombre del sistema operativo subyacente, 
print(pl.system())

#Devuelve una tupla que contiene información sobre el sistema, incluyendo el nombre del sistema operativo, 
# el nombre de la máquina, la versión del sistema operativo, el identificador de la versión y la arquitectura del hardware. 
print(pl.uname())  