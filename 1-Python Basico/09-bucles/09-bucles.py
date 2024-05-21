# Bucles 

# while ( mientras, condicion que requiere condicion para ejecutar)
# y for ( bucle para, que se ejecuta n cantidad de veces)

# El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre.
# El código se ejecutará mientras una condición determinada se cumpla.

x = 5
while x > 0:
    
    # condicion que modifica  la variable x en cada iteración para que la condicion de ingreso cambie y el bucle no sea infinito.
    x -=1
    print(x)
    
 # otro ejemplo   
x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)

# -----------------------------

# condicion de inicializacion para comparar en el while
contador = 0

# condicion de ingreso
while contador < 10:
    print(contador)
    # aumento el contador para que alguna vez termine.
    contador += 1


# break -->  Se utiliza para salir prematuramente de un bucle, deteniendo su ejecución incluso si la condición de control aún es verdadera

print("Break, cuando llega a la condicion sale del bucle.")
contador = 0
while contador < 10:
    print(f"Vuelta numero {contador}")
    contador += 1
    if contador == 5:
        break  # Salir del bucle cuando contador sea igual a 5
print(f"No mostro el contador cuando  es 5 --> mira el valor del contador.-->  {contador}")
print("-----------")
print("\n\n")


#pass: Se utiliza como marcador de posición cuando no se desea ejecutar ningún código dentro de un bloque

# La sentencia pass es similar al null statement (nada), o vacía en otros lenguajes. Es decir, no hace nada y permite la continuidad del flujo
# Ejemplo con pass

print(f"Sentencia pass, no hacer nada cuando contardor sea igual a 5")
contador = 0
while contador < 10:
    if contador == 5:
        pass  # No hacer nada cuando contador sea igual a 5
    else:
        print(f"Vuelta numero {contador}")
    contador += 1
print(f"Cuando el contador vale 5 no hizo nada ")
print("-----------")
print("\n\n")   
#continue: Se utiliza para omitir el resto del código dentro de un bucle y continuar con la siguiente iteración.

print(f"Sentencia continue, que cuando contador sea igual a 5,no ejecuta y sigue a la vuelta de ejecucion siguiente.")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Saltar la impresión cuando contador sea igual a 5
    print(f"Vuelta numero {contador}")
print("-----------")
print("\n\n")


# for, bucle que se repite n cantidad de veces

# aca vamos a usar en el for, un range para que se repita de 0 a 4 ( recordar que los valores arrancan de cero)
for i in range(5):
    print(f"Hola es valor de 'i' en este vuelta es {i}")
print("Fin del primer FOR")
print("-----------")
print("\n\n")



# aca seguimos usando el range, pero le decimos que vaya entre dos mnumeros , no necesariamente usando o arrancando por el 0
# aca va del range  5 al 8-1, osea 5 / 6 / 7    
for i in range(5,8):
    print(f"Hola es valor de 'i' en este vuelta es {i}")
print("Fin del segundo FOR")
print("-----------")
print("\n\n")




# ahora vamos a usar un range con paso 3 
for i in range(0,20,3):
    print(f"Valor de la variable 'i':--> {i} ")

print("\n\n")

# ahora vamos a usar un range con  nunmeros negativos
for i in range(3,-12,-1):
    print(f"Valor de la variable 'i':--> {i} ")

print("\n\n")


# iteracion sobre una lista

lista_nombres=["Pablo","German", "Luis", "Juan"]

for nombre in lista_nombres:
    print(nombre)

print("\n\n")

#Iterar sobre un diccionario (sobre las claves por defecto):
diccionario={"Nombre":"Pedro","Edad":36,"Profesion":"Programador"}
#usando metodo .keys( ) para obtener las llaves y el .values() para los valores.
for key in diccionario.keys():
    print(f"La Clave es : '{key}' , y su Valor es : '{diccionario[key]}'")

print("\n\n")

# otra forma de hacer el anterior
print("Usando metodo clave solo")
for clave in diccionario:
    print("\t")
    print(clave,": ", diccionario[clave])
    
print("\n\n")


# Iterar sobre una lista con índices utilizando enumerate:

lista_dias_semana=["Lunes","Martes","Miercoles","Jueves","Viernes"]

for indice, valor in enumerate(lista_dias_semana):
    print(f"El día de la semana en posición --> {indice}   Es --> {valor}") 

print("\n\n")

# Iterar sobre múltiples iterables simultáneamente utilizando zip:
lista_nombres=["Pablo","Diego","Micaela"]
edad_nombres=[36,35,26]

for nombre, edad in zip(lista_nombres,edad_nombres):
    print(f"La persona que se llama {nombre}, tiene {edad} años.")
    
    
print("\n\n")

# Iterar sobre una secuencia en reversa utilizando reversed:

for nombres in reversed(lista_nombres):
    print(f"Nombres {nombres}")
print("\n\n")

#Iterar sobre los elementos y sus índices utilizando enumerate con un índice inicial:
secuencia = ['a', 'b', 'c', 'd', 'e']
for indice, valor in enumerate(secuencia, start=1):
    print(f"Posicion {indice}, tiene valor de --> {valor}")
print("\n\n")


