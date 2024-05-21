import json 

# Crear un diccionario con listas y diccionarios como valores
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "intereses": ["Python", "Programación", "Data Science"],
    "contacto": {
        "email": "juan@example.com",
        "telefono": "123456789"
    }
}


# convertir el diccionario a formato json

json_data=json.dumps(mi_diccionario,indent=4,separators=(", ",": ") )# indent es para darle formato

with open("datos.json","w") as f:
    f.write(json_data)

print("Archivo guardado")

