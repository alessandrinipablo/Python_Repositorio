### Operadores Aritméticos ###

# Operaciones con enteros

# suma
print(3 + 4)

# resta
print(3 - 4)

# multiplicacion
print(3 * 4)

# division
print(3 / 4)

# modu
print(10 % 3)

print(10 // 3)

# exponenciacion
print(2 ** 3)

# precedencia
print(2 ** 3 + 3 - 7 / 1 // 4)


# operaciones con cadena de texto

print("Hola "+" como"+" Andas?")

# para concatenar el hola con el 5, se tiene que pasar a string prinero.
print("Hola"+ str(5))
print(type(str(5)))

# operaciones mixta

# puedo multiplicar la cantidad de veces un string
print("Hola " * 5)

# aca es igual, multiplica los caracteres por una operacion (2 al 3)
print("Hola " * (2**3))


# se puede hacer comparacion dentro de un print, y devolvera un valor logico.
print(3>4)
print(3<4)
print(3==4)
print(3>=4)
print(3<=4)
print(3!=4)

# operaciones de comparacion con cadenas de texto

print("Hola" > "Python")
print("Hola" < "Python")

print("aaaa" >= "abaa")
print(len("aaaa") >= len( "abaa")) 

print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


# Another way comparison 
print('1 is 1', 1 is 1)                   
print('1 is not 2', 1 is not 2)           
print('A in Asabeneh', 'A' in 'Asabeneh') 
print('B in Asabeneh', 'B' in 'Asabeneh') 
print('coding' in 'coding for all') 
print('a in an:', 'a' in 'an')      
print('4 is 2 ** 2:', 4 is 2 ** 2)   

print(3 > 2 and 4 > 3)  
print(3 > 2 and 4 < 3) 
print(3 < 2 and 4 < 3) 
print(3 > 2 or 4 > 3)  
print(3 > 2 or 4 < 3)   
print(3 < 2 or 4 < 3) 
print(not 3 > 2)     
print(not True)      
print(not False)     
print(not not True)  
print(not not False) 