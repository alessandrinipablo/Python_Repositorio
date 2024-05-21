import json

with open("./datos.json", "r") as f:
    json_data=f.read()
    
data=json.loads(json_data)
print(f"Informacion del archivo Json \n{data}")



# actualizar Archivo Json

with open("./datos.json", "r") as archivo:
    json_data=archivo.read()

data=json.loads(json_data)

data["edad"]=40

# Agregar indentado y separadores para que quede mas bonito el archpersona={"nombre":"Juan","
json_data_actualizado=json.dumps(data,indent=4, separators=("",": ")) 

with open("./datos.json","w") as archivo_2:
    archivo_2.write(json_data_actualizado)