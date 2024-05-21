
"""
Hace: Almacena elementos únicos sin un orden específico.
Tipo de datos guardados: Objetos hashables (números, cadenas, tuplas, etc.).
Características:
    Elementos únicos: No permite duplicados.
    Desordenados: No mantiene un orden específico.
    Mutable: Se pueden agregar y eliminar elementos.
    No indexados: No se puede acceder a los elementos por índice.
    Eficiente para operaciones de conjunto como unión, intersección y diferencia.
Búsqueda eficiente de elementos únicos. """

set1 = {"Juan", "María", "Pedro", "María", "Ana"}
set2 = {"Pedro", "Luis", "Ana", "Sofía"}

print("Conjunto 1:", set1)
print("Conjunto 2:", set2)

# add: Agrega un elemento al conjunto
set1.add("Roger")
print(f"Agregue un elemento al set1 {set1}")  
 
 
# copy: Copia el conjunto
set1 = {1, 2, 3}
set2 = set1.copy()
print(f"Funcion copy ( copia exacta de set ) resultado --> {set2}")

# difference: Devuelve un nuevo conjunto que contiene elementos en set1 pero no en set2

print("-----------------------------------------------------------------------------------\n")
print("Conjunto 1:", set1)
print("Conjunto 2:", set2)
diff = set1.difference(set2)
print(f"Diferencia entre set1/2{diff}")  


print("-----------------------------------------------------------------------------------\n")
# difference_update: Actualiza set1 eliminando los elementos que también están en set2
set1.difference_update(set2)
print(set1)  


print("-----------------------------------------------------------------------------------\n")
# discard: Elimina un elemento específico del conjunto
set1 = {1, 2, 3}
set1.discard(2)
print(set1)  # Salida: {1, 3}
print("-----------------------------------------------------------------------------------\n")

# intersection: Devuelve un nuevo conjunto que contiene elementos que están en ambos conjuntos
intersection = set1.intersection(set2)
print(intersection)  # Salida: set()


print("-----------------------------------------------------------------------------------\n")
# intersection_update: Actualiza set1 para contener solo los elementos que también están en set2
set1.intersection_update(set2)
print(set1)  # Salida: set()
print("-----------------------------------------------------------------------------------\n")
# isdisjoint: Verifica si los conjuntos no tienen elementos en común
disjoint = set1.isdisjoint(set2)
print(disjoint)  # Salida: True
print("-----------------------------------------------------------------------------------\n")
# issubset: Verifica si todos los elementos de set1 están en set2
subset = set1.issubset(set2)
print(subset)  # Salida: True
print("-----------------------------------------------------------------------------------\n")
# issuperset: Verifica si todos los elementos de set2 están en set1
superset = set1.issuperset(set2)
print(superset)  # Salida: False
print("-----------------------------------------------------------------------------------\n")
# pop: Elimina y devuelve un elemento arbitrario del conjunto
elem = set1.pop()
print(elem)  # Salida: 1
print("-----------------------------------------------------------------------------------\n")
# remove: Elimina un elemento específico del conjunto
set1.remove(3)
print(set1)  # Salida: set()
print("-----------------------------------------------------------------------------------\n")
# symmetric_difference: Devuelve un nuevo conjunto que contiene elementos que están en uno de los conjuntos, pero no en ambos
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Salida: {1, 2, 3}
print("-----------------------------------------------------------------------------------\n")
# symmetric_difference_update: Actualiza set1 para contener la diferencia simétrica entre set1 y set2
set1.symmetric_difference_update(set2)
print(set1)  # Salida: {1, 2, 3}
print("-----------------------------------------------------------------------------------\n")
# union: Devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos
union = set1.union(set2)
print(union)  # Salida: {1, 2, 3}
print("-----------------------------------------------------------------------------------\n")
# update: Agrega elementos de otro conjunto al conjunto
set1.update(set2)
print(set1)  # Salida: {1, 2, 3}
print("-----------------------------------------------------------------------------------\n")

# clear: Elimina todos los elementos del conjunto
set1.clear()
print(set1)  # Salida: set()
print("-----------------------------------------------------------------------------------\n")