# Variables

# Buenas practicas
# siempre en minuscula y en snake_case ( entre palabra y palabra va el _ )
# no va guion -, ni caracteres especiales.

# variable en caracter vacio
variable=""
print(variable)

# lista vacia
variable2=[]
print(variable2)

# variable string
nombre="Pablo"
print(nombre)

# metodo snake_case
mi_segundo_nombre="Gabriel"
print(mi_segundo_nombre)

# variable tipo Bool
bandera=True
print(bandera)


# puedo pasar multiples argumentos en el print, tienen que ir separado por comas
print(variable,variable2,nombre,mi_segundo_nombre,bandera)

variable_int=5
variable_int_float=float(variable_int) 
variable_int_str=str(variable_int)  

# muestro los resultados de las variables ( que van a ser iguales a la vista)
print (variable_int,variable_int_float,variable_int_str)

# muestro los tipos de datos de las varibles
print(type(variable_int), type(variable_int_float), type(variable_int_str))

# Funciones del sistema

# funcion len devuelve el tamaño del parametro dado.
print(len("Hola")) 

# solo el len es para string, o lista, o tipo compuesto
# print(len(variable_int))

#pasarle parametros al print

# cuando le pasamos parametros, podemos usar la f, antes de la comilla, y dentro de las comillas entre llaves, va el nombre del parametro
print(f"Mi nombre es {nombre}")

# otra forma , aca va coma despues de la comilla de cierre
print("Usando la coma para pasar variables al print ", nombre)


# variables de una sola linea

name, second_name, surname, age="Pablo","Gabriel","Alessandrini",36

print(f"Nombre -->\t{name}\nSegundo Nombre -->\t{second_name}\nApellido -->\t{surname}\nEdad-->\t{age}")

# guardar datos por entrada (INPUTS)

nombre_usuario=input("Ingrese su nombre por favor: ")
edad_usuario=input("Ingrese su edad por favor: ")

print(f"Su Nombre de usuario es {nombre_usuario} y su edad es {edad_usuario}")


# Tipos y forzando el tipo ( aca no tiene sentido, si lo tiene en los input)

# el : str, es garantizarme que sea string
address: str = "Buena Vista"
print(f"La variable llamada {address} es de tipo {type(address)}")

address: str = True
print(f"La variable llamada {address} es de tipo {type(address)}")

address = 5
print(f"La variable llamada {address} es de tipo {type(address)}")

address = 1.2
print(f"La variable llamada {address} es de tipo {type(address)}")
