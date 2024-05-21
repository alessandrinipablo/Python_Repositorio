# por defecto el modo de abrir un fichero (archivo) es lectura como texto
# por lo tanto para leer su contenido no es necesario especificar el segundo argumento

# r --> read --> r: Abre el archivo en modo lectura. El puntero del archivo se coloca al principio del archivo.
# w --> write--> : Abre el archivo en modo escritura. Si el archivo no existe, se crea. Si existe, se trunca.
# a --> append--> : Abre el archivo en modo escritura, pero no trunca el archivo. En cambio, el puntero del archivo se coloca al final del
#                   archivo. Si el archivo no existe, se crea.
# x --> create--> : Abre el archivo para escritura exclusiva, creando el archivo si no existe. Si el archivo ya existe, la operación fallará.
# t --> text-mode--> : Abre el archivo en modo texto. Este es el modo predeterminado y no necesita ser especificado explícitamente.
# b --> bytes-->  - para archivos como fotosb: Abre el archivo en modo binario. Este modo se usa para archivos binarios, como imágenes 
#                   o archivos de audio.

# abrir un archivo, en este caso un txt ( la lista de temas de Python Basico)


# le paso la ruta, y el metodo que lo voy a abrir en este caso read que es lectura.
file_archivo= open('archivo_txt_prueba.txt','r', encoding='utf-8')
informacion_lectura_archivo=file_archivo

print(f"Informacion de la lectura del archivo {informacion_lectura_archivo}")


# leer contenido
linea=file_archivo.readline( )  # Lee una linea completa hasta el salto de línea
print(f"Primera lina con metodo readline --> Linea: {linea}")


# leer el contendi con readlines
lineas=file_archivo.readlines()    # Lee todas las lineas completas
print(f"Se leen todas las lineas con el metodo readlunes.....\n{lineas}\n")

# para leer todas las lineas con un for, aca en cada salto se pone end="" para que haga correcto el salto de linea
print("Lee todas las lineas completas ")
for i in file_archivo:
    print(i , end="")
    
# SIEMPRE ES BUENA PRACTICA, QUE CUANDO SE ABRE EL ARCHIVO , SE CIERRO
file_archivo.close()
"""
INFORMACION DEL ARCHIVO 
<_io.TextIOWrapper: Indica que el objeto es un TextIOWrapper, que es un tipo de objeto utilizado para leer o escribir texto en un archivo.
name='./archivo_txt_prueba.txt': Esto indica el nombre del archivo que se está manipulando.
está ubicado en el directorio actual (por el './' al principio).
mode='r': Esto indica el modo en el que se está abriendo el archivo. 
'r' significa que el archivo se está abriendo en modo de solo lectura.
encoding='cp1252': Esto indica la codificación de caracteres que se está utilizando para leer el archivo. 
En este caso, 'cp1252' es el nombre de una codificación de caracteres específica (Windows-1252)
que se está utilizando para interpretar los caracteres del archivo.    
"""


# otra forma de abrilo
# al usar with ccuano termino de escribir lineas, dentro, el archivo se cierra solo
print("Usamos el metodo with")
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8') as archivo:
    line=archivo.readlines()
    print(f"{line}")
    
# leyendo con un bucle for
print("Usando un bucle For")
for i in line:
    # vamos a reemplazar el salto de linea con un espacio
    print(i.replace('\n',''))

# eliminamos los saltos de linea y las comillas
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8')  as  archivo_1:
    contenido=archivo_1.read()
    lineas_2=contenido.split('\n')
    lineas_2=contenido.split("''")
    
    print(lineas_2)

# posicion del cursor
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8')  as  archivo_2:
    # para saber la cantidad de caracteres tengo que leer  todo el archivo 
    contenido=archivo_2.read()
    posicion=archivo_2.tell()
    print(posicion)
    print(f"Tamaño del archivo {posicion}")
    
# funcionalidad Seek ( cambia la posicion del cursor, y por ejemplo lee a partir de la posicion 8 en el caso a continuacion)
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8')  as  archivo_3:
    archivo_3.seek(8)
    posicion=archivo_3.tell()
    contenido=archivo_3.read()
    print(contenido)

# leer caracteres por posicion 
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8')  as  archivo_4:
    a_partir_de=archivo_4.read(18)
    print(a_partir_de)
  
# aca va a leer el archivo como string    
with open('./archivo_txt_prueba.txt', "r", encoding='utf-8')  as  archivo_5:
    print(type(archivo_5.read()))
    
# aca va a leer el archivo con bytes
with open('./archivo_txt_prueba.txt', "rb")  as  archivo_6:
    print(type(archivo_6.read()))

# creo un archivo
# si ejecuto el archivo de vuelta, me lo sobreescribe,  pero no elimina el anterior, solo sobreescribe
"""
with open ('./archivo_prueba.txt','w',encoding='utf-8') as archivo_7:
    archivo_7.write('Creacion del archivo con el metodo escritura\nPABLO\nAlessandrini.')

"""

# este metodo no sobreescribe, sino agrega.
with open ('./archivo_prueba.txt','a',encoding='utf-8') as archivo_7:
    archivo_7.write('Creacion del archivo con el metodo escritura\nPABLO\nAlessandrini\nGabriel. ')

print("------------------------------------------") 
import datetime

# Obtener la fecha y hora actual del sistema
fecha_actual = datetime.datetime.now()    
    
#metodo r+
with open ('./archivo_prueba.txt','r+',encoding='utf-8') as archivo_8:
    
    # leo el contenido antes de arrancar 
    contenido_=archivo_8.read()
    print(f"Contenido antes de arrancar {contenido_}")
       
    # quiero agregar contendio al incio del archivo
    
    #muevo el cursor al inicio
    archivo_8.seek(0)
    
    # Obtener la fecha y hora actual del sistema
    fecha_actual = datetime.datetime.now().time()
    
    cadena_formateada = fecha_actual.strftime("%H:%M:%S")
    archivo_8.write( cadena_formateada)
    
    # Mover el puntero al inicio del archivo nuevamente
    archivo_8.seek(0)
    
    # Leer y mostrar el contenido actualizado del archivo
    print("\nContenido del archivo después de escribir:")
    print(archivo_8.read())