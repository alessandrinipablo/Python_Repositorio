# Funciones 
# Funciones: Las funciones en Python son bloques de código reutilizable que realizan una tarea específica. 
#            Se definen con la palabra clave def seguida del nombre de la función y los parámetros entre paréntesis.

# Parámetros: variables definidas en la declaración de una función, 
# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos: mientras que los argumentos son los valores reales que se pasan a la función cuando se la llama. 
#            Los argumentos son asignados a los parámetros en el orden en que se pasan.
# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos opcionales: En Python, los argumentos de una función pueden tener valores predeterminados,
#                        lo que los convierte en argumentos opcionales. Esto significa que puedes llamar a la función sin proporcionar 
#                        valores para estos argumentos, y se utilizarán los valores predeterminados.
# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos nombrados: También conocidos como argumentos con nombre, te permiten pasar los argumentos a una función utilizando el nombre
#                       del parámetro al que corresponde el valor. Esto puede hacer que el código sea más legible y menos propenso a errores.
# -------------------------------------------------------------------------------------------------------------------------------------
# "  *args: Es una sintaxis en Python que te permite pasar un número variable de argumentos a una función. 
#           Los argumentos se recopilan en una tupla y puedes acceder a ellos dentro de la función utilizando el nombre del parámetro precedido 
#    por un asterisco (*).
# -------------------------------------------------------------------------------------------------------------------------------------
#"   **kwargs: Similar a *args, pero para argumentos con nombre. Te permite pasar un número variable de argumentos con nombre a una función, 
#              que se recopilan en un diccionario. Puedes acceder a estos argumentos dentro de la función utilizando el nombre del parámetro 
#              precedido por dos asteriscos (**).
# -------------------------------------------------------------------------------------------------------------------------------------
#     return: La palabra clave return se utiliza para devolver un valor desde una función. Puedes devolver uno o varios valores, 
#             y la ejecución de la función termina en ese punto.
# -------------------------------------------------------------------------------------------------------------------------------------
#    Alcance: El alcance en Python se refiere a la visibilidad y accesibilidad de las variables en diferentes partes del código.
#    Existen dos tipos principales de alcance: 
#    alcance local  -->  que se refiere a las variables definidas dentro de una función, 
#    alcance global --> que se refiere a las variables definidas fuera de cualquier función.
# -------------------------------------------------------------------------------------------------------------------------------------
#    Depurando funciones: La depuración de funciones implica identificar y corregir errores en el código de una función utilizando 
#    herramientas de depuración como puntos de interrupción, impresiones de depuración y analizadores de código.
# -------------------------------------------------------------------------------------------------------------------------------------

# Creacion de funciones, si bien no importa el orden, siempre se trata de crearlas al principio y todas juntas.

# creo una funcion simple, sin parametros ni argumentos.
def mensaje():
    print("Hola mundo")

# funcion 
def espacios():
    print("\n\n")
    print("---------------------")
    print("\tOtra ejecucion\n")

# funcion 
# para poder usarlo dentro de algo, tiene que retornar algo 
def mensaje_2():
    return "Hola mundo"


# creacion de funcion con 1 parametro 
#  parametros 
def saludo (nombre):
    print(f"Hola como estas {nombre}")
    
    

# funcion con dos parametros o mas
def saludo_nombre_apellido (nombre, apellido):
    print(f"Hola soy {nombre} y mi apellido es {apellido}")
    
    
# creacion de funcion con parametros opcionales, es porque si al momento de llamarla no se pasamos valor, toma el parametro de que se paso en la funcion.
def saludar_parametros_opcionales(nombre="funcion con parametros opcionales"):
    print(f"Hola como estas '{nombre}' ")


# funcion con Argumentos nombrados, esto es porque al momento de llamar la funcion en el cuerpo del codigo, y no recuerdo el order
# al momento de invocarlas, le digo que que el argumento x= name, argumento Y = age
def saludo_argumentos_nombrados(name, age):
    print(f"Hola como andas {name} es cierto que tenes {age} años?")


# funcion con xargs
def suma (*numeros) :
    resultado=0
    for numero in numeros:
        resultado += numero
    print(resultado)
    
    
# funcion con kwargs
def mostrar_valores(**datos):
    print(datos)
    
# otro ejemplo de funcion con multiples argsms
def detalles(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
        
        
# funcion con Return
def normalizar_minusculas(frase):
    return frase.lower()

# alcance de las funciones ( variables locales,y globales) no se deben usar, son malas practicas

# -----------------------------------------------------------------------------
# cuerpo principal donde llamos a las funciones


# llamado a la funcion
# quiero que la funcion se ejecute 3 veces  y llamo a la funcion
for i in range(3):
    print(f"Ejecucion numero {i+1}")
    mensaje()
espacios()



# Quiero que la función se ejecute 3 veces
# y llamo a la función dentro de un print
for i in range(3):
    print(f"Ejecución número {i+1}: {mensaje_2()}")
espacios()   



# uso de la funcion con argumentos
nombres=["Pablo","Diego","Micaela"]
for i in nombres:
    saludo(i)
    
espacios()

dato={"Pablo":"Alessandrini"}
for clave, valor in dato.items():
    saludo_nombre_apellido(clave, dato[clave])
    
espacios()

#llamado a la funcion saludar_con_parametros_opcionales
# sin parametros
print("Llamo a la funcion  sin parametros")
saludar_parametros_opcionales()

# con parametros
nombre="Pablo"
print("A la funcion con parametros opcionales decido darle un nombre, o sea le paso parametros")
saludar_parametros_opcionales(nombre)

espacios()

# llamado a la funcion argumentos nombrados
saludo_argumentos_nombrados(name="Joaquin", age=78)
espacios()

# llamado a la funcion con xargs

#lista_numeros=[0,58,45,9]
# llamo a la funcion con xargs y le paso diversos valores.
suma(0,58,45,9)
suma(1,2,3,4,5)

espacios()

# llamada a la función  mostar_valores
print("Llamado a una funcion que tiene kwargs")
mostrar_valores(nombre="Pablo", segundo_nombre="Gabriel", apellido="Alessandrini")


espacios()
# llamada a la segunda funcion de kwargs
print("Llamada a funcion 2 de multiples args ..> kwargs ( en la funcion se uso un for para recorrer los multiples args)")
detalles(nombre="Pablo", segundo_nombre="Gabriel", apellido="Alessandrini")
espacios()

# llamado a la funcion normalizar minusculas 

dato="PaBlO Alessandrini Gabriel"
dato=normalizar_minusculas(dato)
print(f"El nombre normalizado quedo de la siguiente manera {dato}")

espacios()
