# Ejemplo de como funcionan los 'dictionary' 

# Definir un diccionario
curso = {
    "nombre": "Introducción a la programación",
    "semestre": "2019S2",
    "anio": 2019,
    "institucion": "CIDE"
    }
print(curso)               # Imprime todo el dictionary
print(curso["nombre"])     # Imprime: Introducción a la programación
print(curso.get("nombre")) # Imprime: Introducción a la programación

# Hacemos un ciclo sobre las llaves
for v in curso: #Loop de los keys
    print(v)
    
# Hacemos un ciclo sobre los valores 
for v in curso.values():
    print(v)
    
# Hacemos un ciclo sobre parejas 'key-value' (lo más útil)
for k,v in curso.items(): #Loop de key-value-pairs
    print(k,v,sep="=>")
    

# También podemos consultar si (o no) existe un 'key'  
if "profesor" not in curso: # Ver si un key existe (o no) en un dictionary
    curso.update({"profesor":"desconocido"}) #Agregar/actualizar un key-value-pair

print(curso)
    

