# Write to json

# Import the requires package
import json

# Generate a complex dictionnary
curso1 = {
    "nombre": "Introducción a la programación",
    "semestre": "2019S2",
    "anio": 2019,
    "institucion": "CIDE"
    }

curso2 = {
    "nombre": "Modelos basados en agentes",
    "semestre": "2019S2",
    "anio": 2019,
    "institucion": "CIDE"
    }

datos = {
    "titulo": "lista de cursos 2019S2",
    "cursos": [curso1,curso2]}

# Print it to the console (not needed,but helpful)
print(datos)

# Open a file and convert the dictionnary to a json string
with open("lista_cursos.json",'w') as f:
    json.dump(datos,f)
    
    
    
    
    
    
    
    
    
    
    
    
    
    