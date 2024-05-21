# condicionales
# operadores de comparacion 
# > mayor que
# < menor que
#  == igual a
# <= menos o igual a
# >= mas o igual a
# "" != no es igual a 
# not negar una condicion
condicion=True

# if condicion: es igual a --> condiccion==True:
if condicion:
    print("Ingreso por el verdadero,  la variable es True")
    

# if /else

#condicion_=True
condicion_=False
if condicion_:
    print(condicion_)
else:
    print(condicion_)

# if-elif-else

edad=int(input("Ingresa tu edad por favor en nunmeros: "))  

if edad>18:
    print("Mayor de edad") 
#elif  edad==18:
  #  print("Es mayor de edad pero no tiene la mayoria")
else:
    print("Es menor de edad")    

# Operador ternario: Permite escribir condicionales de forma más compacta en una sola línea.
nombre="Pablo"
segundo_nombre="Pablo_Gabriel"
resultado = nombre if nombre=="Pablo" else segundo_nombre

print(f" El resultado es {resultado}")


# Condicionales cortocircuitados: 

# Ejemplo de condicional cortocircuitado con and
x = 5
y = 10
resultado = "Ambos son mayores que 5" if x > 5 and y > 5 else "Al menos uno no es mayor que 5"
print(resultado)

# Ejemplo de condicional cortocircuitado con or
valor = None
valor = valor or "Valor predeterminado si valor es None"
print(valor)

points=15
match points:
    case 0:
        print("0")
    case 15:
        print("15")
    case 30:
        print("30")
    case 45:
        print("45")
    case _:
        print("Error")

# Comprobación de pertenencia con in:

lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("El número 3 está en la lista")
 
 
#Comprobación de existencia con is:   
x = [1, 2, 3]
y = [1, 2, 3]
if x is y:
    print("x y y son el mismo objeto")
else:
    print("x y y son objetos diferentes")