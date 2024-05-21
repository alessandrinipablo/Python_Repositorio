"""#1. **SyntaxError:**
#      - Ocurre cuando hay un error de sintaxis en el código Python, como una falta de comillas, paréntesis mal cerrados, etc.
2. **IndentationError:**
#    
3. **NameError:**
#   - Ocurre cuando se intenta usar una variable o función que no está definida en el ámbito actual.#
4. **TypeError:**
#   - Ocurre cuando se intenta realizar una operación en un tipo de dato incorrecto.
5. **IndexError:**
#   - Ocurre cuando se intenta acceder a un índice fuera del rango válido en una lista, tupla o array.
6. **KeyError:**
#   - Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
7. **ValueError:**
#   - Ocurre cuando se pasa un argumento con un valor incorrecto a una función.
8. **FileNotFoundError:**
#   - Ocurre cuando se intenta abrir un archivo que no existe.
9. **ZeroDivisionError:**
#   - Ocurre cuando se intenta dividir un número por cero.
10. **ImportError:**
#    - Ocurre cuando hay un problema al importar un módulo.
11. **AttributeError:**
#    - Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
12. **EOFError:**
#    - Ocurre cuando se llega al final de un archivo o entrada de datos inesperadamente.
13. **KeyboardInterrupt:**
#    - Ocurre cuando se presiona Ctrl+C para interrumpir la ejecución del programa desde la consola.
14. **MemoryError:**
#    - Ocurre cuando no hay suficiente memoria disponible para ejecutar el programa."""


# eventos produciodos en la ejecucion de un programa, y puede provocar detencion del error.

# exepcion name error querer llamar a una variable que no existe
#print(a)

# exepcion value error
#print(int("Error de querer pasar un string que no sea numero a Entero."))

# index error, acceder a un indice que esta fuera de rango
#lista=[1,2,3]
#print(lista[3])  

# key error, intentar buscar una llave que no existe en un diccionario
#dic={"uno":1,"dos":2}
#print(dic["tres"]) 

# type error de querer sumar un string + un entero
# print("Hola" + 3)

# error de sintaxis SyntaxError: expected ':'
#if True
#print("Es verdad")

# IndentationError: expected an indented block after 'if' statement on line 53
# if  False:


# Zero division error --> ZeroDivisionError: division by zero

#print(10/0)

# OS error  --> OSError: [Errno 22] Invalid argument: 'archivo*cualquier'
# FileNotFoundError: [Errno 2] No such file or directory: 'archivocualquier'
#with open ("archivo*cualquier", "r") as archivo:
#    pass

# bloques
# try except  finally son  bloques de control de flujo de programacion para capturar errores 

# se puede poner un excpet, o varios tipos de except
def dividir(num1, num2):
    try:
        #intentamos realizar la division
        resultado=num1 / num2
        print(f"La división es {resultado}")
    except Exception as e:
      
        print(f"Se produjo un error, no se puede seguir,  error tipo-->  {e}")
        print("\tHa habido una excepción", type(e))
        
    finally:
        print("Fin del programa")

#dividir(10,"q")


# otro forma de  tipo de expeciones

try:
    # Se fuerza excepción
    x = 2/0
except Exception as t:
    print(f"Entra en except, ha ocurrido una excepción {t}")
else:
    # el else es sino ocurre ninguna expecion sigue por el elsse
    print("Entra en el else, no ha ocurrido ninguna excepción")
    
finally:
    print("Entra en finally, se ejecuta el bloque finally")

# asserte

def calcular_area_rectangulo(ancho, alto):
    
    # Verificar que el ancho y el alto sean números positivos
    # condicion  con assert, y  si no se cumple lanza AssertionError
    assert ancho > 0, "El ancho debe ser un número positivo"
    assert alto > 0, "El alto debe ser un número positivo"
    
    # Calcular el área del rectángulo
    area = ancho * alto
    
    return print(f"EL area es {area}")

# Ejemplos de uso
#print(calcular_area_rectangulo(5, 4))  # Salida: 20
print(calcular_area_rectangulo(-3, 4))  # Genera un AssertionError