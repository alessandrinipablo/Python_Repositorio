# Listas --> Una lista en Python es una colección ordenada y mutable de elementos. Puedes pensar en ella como una secuencia 
# de elementos separados por comas y encerrados entre corchetes [].

lista=[]
lista_2=list()

print(type(lista))  
print(type(lista_2)) 

# funcion len tambien para listas

print(len(lista))   
print(len(lista_2))

my_list= [35, 24, 62, 52, 30, 30, 17]

print(my_list)

# tamaño
print(f"Tamaño de mi lista llamada my_list es {len(my_list)}")

# acceder a elmentos por indice
print(my_list[0])
print(my_list[1])
print(my_list[-4])
print(my_list[-3])

# invertir la lista
print(my_list[::-1]) 


#cuenta cuantas veces aparece un elemento en una lista si no  esta devuelve 
print(my_list.count(300))                             

# si el elemento no esta devuelve error
# print(my_list[300])

# usando la funcion index, se puede pasar el parametro de un elemento y devuelve la posicion, si no esta da error
# print(my_list.index("Brais"))
print(my_list.index(24))


lista_2=[35, 1.98, "Pablo", "Alessandrini"]
edad, altura, nombre, apellido=lista_2

print(edad)
print(altura)
print(nombre)
print(apellido)

edad, altura, nombre, apellido = lista_2[3],lista_2[1],lista_2[0],lista_2[2]

print(f"Asignando valores a la lista, pero por posicion  {edad} ")

# concatenar Listas

l1=[1,2,3,4,5]
l2=[8521,111,15]

# se pueden concatenar dos listas o mas 
# pero no se pueden restar( signo - )
print(l1+l2) #concatenacion
# print(l1-l2)



# funciones para lista, con mumeros
lista_a=[1,2,3,4,5]
print("-----------------------------------")
print(f"La suma de la lista {lista_a} es {sum(lista_a)}")
print (f"El maximo valor de la lista {lista_a} es {max(lista_a)}")
print (f"El minimo valor de la lista {lista_a} es {min(lista_a)}")
print(f"El tamano de la lista {lista_a}  es {len(lista_a)}")


#1- funcion --> append(): Agrega un elemento al final de la lista.
lista_nombres= ["Argentina", "Brasil", "Canadá", "Francia", "Japón"]
print("-----------------------------------")
print(f"Funcion append, agrega un elemento al final de la lista\nLista antes del append --> {lista_nombres}")
lista_nombres.append("Usa")
print(f"Lista actualizada despues de append {lista_nombres}")


#2- funcion --> remove(): Elimina la primera ocurrencia de un elemento específico de la lista.
print("-----------------------------------")
print(f"Lista antes de aplicar la funcion remove --> {lista_nombres}")
lista_nombres.remove("Usa")
print(f"Lista luego de aplicar remove {lista_nombres}")

#3- funcion --> pop(): Elimina y devuelve el último elemento de la lista o el elemento en la posición especificada.
print("-----------------------------------")
print(f"Lista  actual {lista_nombres}")
lista_nombres.pop()
print(f"El remove sin pasarle el indice, elimina la ultima posicion\n {lista_nombres} ")
lista_nombres.pop(0)
print(f"Funcion pop pasando indice, elimina segun el mismo,\n {lista_nombres}")


#4- funcion insert(): Inserta un elemento en una posición específica de la lista.
print("-----------------------------------")
print(f"Lista  actual {lista_nombres}")
# tiene dos parametros, la posicion y lo que se va a insertar
lista_nombres.insert(2,"México")
print(f"Lista actualiza, en la pos -- > 2 se va a insertar Mexico\n {lista_nombres}")



#5- funcion extend(): Extiende la lista agregando todos los elementos de otra lista al final.
print("-----------------------------------")
lista_agregada=["Alemania","España"]
lista_nombres.extend(lista_agregada)
print(f"La lista que se agrega {lista_agregada} La lista actualiza {lista_nombres}" )


print("-----------------------------------")
#6- funcion index(): Devuelve el índice de la primera ocurrencia de un elemento en la lista.
resultado=lista_nombres.index("Francia")
print(f"La funcion index con el parametro Francia devuelve {resultado}")
#resultado_2=lista_nombres.index("China")
# print(f"La funcion index con el parametro China devuelve {resultado_2}")


print("-----------------------------------")
#7- funcion --> sort(): Ordena los elementos de la lista en su lugar (sin devolver una nueva lista).
print(f"Lista como esta antes de aplicar sort -->{lista_nombres}")
lista_nombres.sort(reverse = False) 
print(f"Lista ordenada con reverse False --> {lista_nombres}")
lista_nombres.sort(reverse = True) 
print(f"Lista con reverse en true -->{lista_nombres}")


print("-----------------------------------")

#8- funcion --> reverse(): Invierte el orden de los elementos de la lista en su lugar.
print(f" Lista antes del Reverse {lista_nombres}")
lista_nombres.reverse()
print(f"Aplicando reverse  {lista_nombres}")


print("-----------------------------------")
#9- funcion --> count(): Devuelve el número de veces que un elemento aparece en la lista.
print(f" Lista original {lista_nombres}")
cantidad_brasil=lista_nombres.count("Brasil")
print(f"Existe Brasil {cantidad_brasil} Veces")
cantidad_argentina=lista_nombres.count("Argentina")
print(f"Existe Argentina {cantidad_argentina} Veces ")


print("-----------------------------------")
#10- funcion --> clear(): Elimina todos los elementos de la lista.
lista_nombres.clear( )   #Eliminamos todo lo que hay en la lista
print(f"Lista vacia {lista_nombres}")


print("-----------------------------------")
#11- Funcion del metodo que hay que pasar lista y la posicicion a elimniar
my_lista=[5,4,3,2,1]
del my_list[2]
print(my_list)


print("-----------------------------------")
# funcion copy, que hace una copia exacta de la lista
my_new_list = my_list.copy()
print(f"Lista original --> {my_list}")
print(f"Lista copia  --> {my_new_list}")



print("-----------------------------------")
# Sublistas
print(my_new_list[1:3])