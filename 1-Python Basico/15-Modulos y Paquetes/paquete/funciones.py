# funcion que devuelve el factorial de un numero
# como este archivo pertenece a un paquete, si o si en la carpeta del paquete tiene que haber un archivo que diga __init__.py 
# python lo va a tomar como que es un paqeute

def factorial (n):
    facto=1
    for i in range(1,(n+1)):
        facto*=n
    return facto

nombre_autor="Pablo Alessandrini"