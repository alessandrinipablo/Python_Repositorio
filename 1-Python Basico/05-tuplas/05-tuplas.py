# Una tupla en Python es una colección ordenada de elementos, similar a una lista, pero con la diferencia clave de que las tuplas son inmutables,
# lo que significa que una vez creadas, no se pueden modificar, agregar o eliminar elementos de ellas.

# creacion de tupla

tupla=tuple()
tupla_2=()
# verificacion del elemento creado
print(f"Tipo de dato de la tupla llamada tupla   {type(tupla)}")
print(f"Tipo de dato de la tupla llamada tupla_2 {type(tupla_2)}")

tupla=("Pablo","Gabriel","Alessandrini",36,1.97)
tupla_2=(35,36,37)

print(f"Tupla 1 --> {tupla}")
print(f"Tupla 2 --> {tupla_2}")

# acceso a elementos

print(f"Acceso a elemento en posicion 0 {tupla[0]}")
print(f"Ultimo elemento {tupla[-1]}")
print(f"Penultimo elemento {tupla[-2]}")
# fuera de rango da error
# print(f"Acceso a elemento en posicion 0 {tupla[10]}")

# count
resultado=tupla.count("Pablo")
resultado2=tupla.count("Juan")
print(f"Contado las veces que aparece Pablo {resultado}")
print(f"Contado las veces que aparece Juan  {resultado2}")

# index

print(f"Usando la funcion index, buscando en que posicion esta el valor Pablo\nposicion -->  {tupla.index('Pablo')}")


# concatenacion de dos tuplas 
tupla_total= tupla+tupla_2

#restar_tuplas=tupla-tupla_2
print(f"Concatenacion de dos tuplas {tupla_total}")
#print(f"Resta de dos tuplas {restar_tuplas}")


# subtuplas

print(f"Mostrar parte de la tupla (1 a 4)\t {tupla_total[1:4] } ")
print(f"Mostrar parte de la tupla (total)\t {tupla_total[:] } ")
print(f"Mostrar parte de la tupla (final para atras)\t {tupla_total[-1:] } ")
print(f"Mostrar parte de la tupla ( antepenultmimo)\t {tupla_total[-3] } ")



# Tupla mutable con conversión a lista

#conversión de tupla a lista
mi_tupla=list(tupla_total) 
print(type(mi_tupla))

mi_tupla[4]="Agregar un elemento a la lista(TUPLA)"

mi_tupla=tuple(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)


# la tupla no se pueden eliminar elementos.
# del  mi_tupla[5]
print(mi_tupla)

#se puede agregar o editar los valores pero no eliminarlos



