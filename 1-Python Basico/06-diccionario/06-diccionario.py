# Los diccionarios en Python son una estructura de datos que permite almacenar pares clave-valor. 
# las claves deben ser únicas e inmutables, lo que significa que no pueden cambiar una vez definidas, 
# y los valores pueden ser de cualquier tipo de datos, incluyendo números, cadenas de texto, listas, tuplas u otros diccionarios.




# creacion de diccionario vacio 

#forma 1:
mi_diccionario=dict()

#forma 2:
mi_diccionario_otra_manera={}

# verificamos que tipo de elemento se creo ( verificamos que sea diccionario)
print("Tipo de elemento del Primer diccionario --> ",type(mi_diccionario))
print("Tipo de elemento del Segundo diccionario --> ",type(mi_diccionario_otra_manera))

mi_diccionario={"Nombre":"Pablo",
                "Apellido":"Alessandrini",
                "Edad":1,
                "Lenguaje":"Python"}

# muestro el diccionario
print(f"Muestro mi diccionario:  \n {mi_diccionario}")

# tamaño del diccionario (pares de claves-valor
print(f"Tamaño del diccionario {len(mi_diccionario)}")


#busqueda por elemento y por indice

#pasando indice me da error , ya que es por clave -valor
# print(f"Valor del elemento en la primer posicion, n=1 {mi_diccionario[1]} ")
#pasando el valor a buscar da error tambien 
# print(mi_diccionario["Pablo"])

# paso valores respecto a las claves de los diccionarios, y devuelven si estan o no en el mismo como valor booleano.
print("Pablo" in mi_diccionario)
print("Nombre" in mi_diccionario)
print(1 in mi_diccionario)

mi_diccionario_original = {"a": 1, "b": 2}

# copia exacta del diccionario original
mi_diccionario_copia=mi_diccionario_original.copy()

print(f"Diccionario original: --> {mi_diccionario_original}")
print(f"Diccionario copia exacta: --> {mi_diccionario_copia} ")


# get(): Devuelve el valor asociado a una clave dada. Si la clave no existe, devuelve un valor predeterminado.
valor=mi_diccionario.get("Nombre")
valor2=mi_diccionario.get("Fecha de Nacimiento")
print(f"Se pasa una clave y devuelve el valor asociado 'Clave' --> 'Nombre' es:{valor} ")
print(f"Cuando no encuentra el valor de la clave, devuelve --> {valor2} ")


# diccionario para practicar 
datos_personas = {
    "Juan": {"Edad": 30, "Ciudad": "Madrid", "Profesión": "Ingeniero"},
    "María": {"Edad": 25, "Ciudad": "Barcelona", "Profesión": "Doctora"},
    "Carlos": {"Edad": 35, "Ciudad": "Sevilla", "Profesión": "Abogado"},
    "Ana": {"Edad": 28, "Ciudad": "Valencia", "Profesión": "Profesora"},
    "Pedro": {"Edad": 40, "Ciudad": "Bilbao", "Profesión": "Arquitecto"},
    "Laura": {"Edad": 33, "Ciudad": "Málaga", "Profesión": "Diseñadora"},
    "Pablo": {"Edad": 27, "Ciudad": "Alicante", "Profesión": "Programador"},
    "Sofía": {"Edad": 29, "Ciudad": "Zaragoza", "Profesión": "Contadora"}
}

# keys
print(f"Claves del diccionario llamado datos_personas\n {datos_personas.keys()}")

# valores
print(f"Valores del diccionario 'datos_personas' {datos_personas.values()}")


# items (muestra las claves / valor )
print(f"Item del diccionario datos_personas {datos_personas.items()}")

# get devuelve el valor asignado a una clave, si no encuentra nada, devuelve None
valor_clave="Pablo"
valor_clave2="Diego"

valor_encontrado=datos_personas.get(valor_clave)
valor_encontrado_2=datos_personas.get(valor_clave2)

print(f"El valor encontrado para la clave '{valor_clave} es --> {valor_encontrado}")
print(f"Si busco por '{valor_clave2}' pero no existe en el diccionario, me devuelve--> {valor_encontrado_2}")


# pasando por clave

print(f"Pasando la clave como parametro el valor es: -->  {datos_personas['Juan']}")

# si paso una clave que no tiene , o no existe la clave da error.

# list --> devuelve una lista con los valores del diccionario 

lista_valores=list(datos_personas.values())
print(f"Conversion del diccionario a lista, con solo los valores  --> {lista_valores}")

# pasando el diccionario como parametro de una lsita, devuelve una lista con las claves.
lista_valores_2=list(datos_personas)
print(f"Convirtiendo el diccionario en una lista {lista_valores_2}")

# len tamaño del diccionario 
print(f"Tamaño del diccionario {len(datos_personas)} pares")


mi_diccionario_original = {"a": 1, "b": 2}

# paso las claves y me devuelve si es verdadero o falso estando o no en el diccionario
print(1 in mi_diccionario_original)
print("a" in mi_diccionario_original)

# negando si esta o no
print(1 not in  mi_diccionario_original)
print("a" not in mi_diccionario_original)

# iter 
valores=iter(datos_personas)
print(f"Funcion iter --> {next(valores)}")

# reversed
diccionario_reverso=reversed(datos_personas.keys())
print(f"Diccionario en forma reversa {next(diccionario_reverso)}")


# diccionario vacio
equipos=dict()

print(type(equipos))


# insercion
print(f"Diccionario vacio {equipos}")
equipos["Nombre"]="Racing"

print(f"Diccionario con la primera insercion {equipos}")
valor_dic=equipos["Nombre"]
print(f"Pasando la clave como parametro para que devuelva el valor --> '{valor_dic}' ")

# actualizacion
print(f"Antes de actualizar el diccionario {equipos}")
equipos["Nombre"]="Racing Club de Avellaneda"
valor_clave=equipos["Nombre"]
print(f"Luego de actualizar el valor de la clave 'Nombre' {valor_clave}")

# eliminacion 

del equipos["Nombre"]
print(f"Diccionario elimnando la clave 'nombre' {equipos}")

pais = {
    "Nombre": "Argentina",
    "Capital": "Buenos Aires",
    "Poblacion": 45195774,
    "Idioma": "Español",
    "Moneda": "Peso argentino"
}

print(f"Diccionario Pais --> {pais}")
print(f"Funcion items --> {pais.items()}")
print(f"Funcion Keys   -->{pais.keys()}")
print(f"Funcion Values  --> {pais.values()}")


# lista de datos de paises limitrofes de argentina

paises = ["Brasil","Uruguay","Paraguay","Chile","Bolivia"]
capitales=["Brasilia","Montevideo","Asuncion","Santiago de Chile","La Paz"]

print(f"Lista con datos de paises limitrofes de argentina")

nuevo_dict=dict.fromkeys(paises)
print(f"Lista transformada a diccionario {nuevo_dict}")

#creando un diccionario con dos listas
paises_capitales = dict(zip(paises, capitales))

print(f"Pais creado {paises_capitales}")



# Crear un diccionario de ejemplo
nuevo_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1}

valores_nuevo_dict=nuevo_dict.values()

print(type(valores_nuevo_dict))
print(f"Valores del diccionario {valores_nuevo_dict}")


# Obtener una lista de valores únicos del diccionario

valores_unicos = list(dict.fromkeys(valores_nuevo_dict).keys())
print("Valores únicos del diccionario:", valores_unicos)

# Convertir las claves del diccionario en una tupla
keys_tupla = tuple(nuevo_dict)
print("Claves convertidas en una tupla:", keys_tupla)

# Convertir las claves del diccionario en un conjunto
keys_set = set(nuevo_dict)
print("Claves convertidas en un conjunto:", keys_set)


#---------
print("------------------")


# update(): Actualiza el diccionario con elementos de otro diccionario u otra iterable.
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4}

print(f"Diccionario  1 -->  {diccionario1}")
print(f"Diccionario  2 -->  {diccionario2}")

diccionario1.update(diccionario2)

print(f"Diccionario 1 actualizado con diccionario 2 {diccionario1}")


#---------------
# pop(): Elimina y devuelve el valor asociado a la clave especificada del diccionario.

valor_eliminado= nuevo_dict.pop('a')
print(f"Funcion pop que elimina el valor de la clave dada por parametro\n valor cuando existe la clave-- > {valor_eliminado}")


# clear(): Elimina todos los elementos del diccionario.

diccionario_prueba = {"a": 1, "b": 2}
print(f"Diccionario prueba {diccionario_prueba}")
diccionario_prueba.clear()
print(f"Diccionario eliminado {diccionario_prueba}")  

