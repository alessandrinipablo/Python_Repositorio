# String (cadena de caracteres)

nombre="Pablo"
segundo_nombre="Gabriel"

print(f"Tamaño o cantidad de letras de la variable {nombre} son {len(nombre)}") 
print(f"Tamaño o cantidad de letras de la variable {segundo_nombre} son {len(segundo_nombre)}") 


# concatenar string, para que quede prolijo se lo concantena con un espacio, que al fin y al cabo tambien es caracter
nombre_concatenado=nombre+" "+ segundo_nombre
 
print(f"Concatenar en el print {nombre} {segundo_nombre}")
print(f"Mostrar la variable contaneda {nombre_concatenado}")
print(nombre+ " "+ segundo_nombre)


# caracteres de control de salto de línea
string_salto_linea="Cadena de caracteres con salto de linea \n"
retorno_de_carro="String con retorno de carro  \r"
retroceso="String con retroceso \b"
tabulacion="\tString con tabulacion"
caracter_nulo="Strin de caracter nulo \0"

# los caracteres de escapado es poner otra barra mas en los caracteres de salto de linea, siendo que esta ultima anula los mismos.
escapado="\tCaracter escapado \\n caracter"
lista_caracteres_salto_linea=[string_salto_linea,retorno_de_carro,tabulacion,retroceso,caracter_nulo,escapado]
for i in lista_caracteres_salto_linea:
    print(i)
    
# formateo ( COMO MUESTRO POR PANTALLA STRING)
name="Pablo"
second_name="Gabriel"
surname="Alessandrini"
# diferentes formas de mostrar los print de pantallas usando format
print(f"Me llamo  {name} {second_name} {surname}.")
print("Me llamo "+name+second_name+surname+".")
print("Me llamo {} {} {} ".format(name, second_name, surname))
print("Me llamo %s %s %s "%(name, second_name, surname))


# desempaquetando caracteres
language="Python"

a,b,c,d,e,f=language
print(a)
print(e)


# slicing 

# el slicing es rebanar, tomar parte de la cadena de caracteres
# tiene tres partes (inico:fin:paso )
print(language[1:3])
print(language[:-1])
print(language[-1:])

print(language[-2])

#reverse

print(language[::-1])

#Funciones del lenguaje para string

print(f"Capitalize --> {language.capitalize()} ") 
print(f"Upper --> {language.upper()}") 
print(f"Count  --> {language.count('P')}")
print(f"Is numeric -->  {language.isnumeric()}")
print(f"Lower --> {language.lower()}") 
print(f"Lower  y ver si es upper.{language.lower().isupper()}")
print(f"Comienza con {language.startswith('P')}")
print(f"termina con {language.endswith('n')}")
print(f"Find 'y' en language --> {language.find('y')}")
print(f"Tiene espacios? --> {language.isspace()}")
print(f"Es alfanumerico?--> {language.isalnum()}")
print(f"Caracteres imprimibles? --> {language.isprintable()}")
