import json

archivo_json_prueba ='{"nombre":"Pablo","edad":36, "pais":"Argentina"}'
print(f"Mostrando el archivo JSON {archivo_json_prueba}")
print(f"Tipo de archivo creado {type(archivo_json_prueba)}")

#Convierte una cadena JSON en un diccionario Python
python_dict=json.loads(archivo_json_prueba)
print(python_dict)
print(type(python_dict))


# acceder a una clave
print(python_dict['edad'])

# otra forma

data={
    'name': 'John', 
    'age': 30, 
    'city': 'New York',
    # crear un una clave valor( lista)
    'cursos':['Python','sql','Power Bi','Html','Css','Data Science','Javascript']
    }
# creo el archivo json, y le paso parametros para  que se lea mejor
# indentacion, separadores y que ordene las llaves
json_data=json.dumps(data, indent=4, separators=(", ",": "), sort_keys=True)

print(f"Imprimo el archivo JSON {json_data}")
print(f"Tipo de archivo {type(json_data)}")


json_data_2=json.JSONEncoder().encode({"lenguajes":["Python","JS"]})
print(json_data_2)
print(type(json_data_2))

python_diccionario=json.JSONDecoder().decode(json_data_2)
print(python_diccionario)
