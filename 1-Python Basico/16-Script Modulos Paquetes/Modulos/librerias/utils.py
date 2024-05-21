import math 
from random import randint

def raizCuadrada(numero):
    return print(f"La raiz cuadrada de {numero} es {math.sqrt(numero)}")

def numeroAletorio(a,b):
    resultado=randint(a,b)
    return print(f"El numero aleatorio es {resultado}")