#Ejercicio de una lista de participantes

participantes =[]
print(type(participantes))

# Recibir la informacion
entrada =""
while entrada!="end":
    print("Favor de poner su nombre:")
    entrada = input()
    if entrada=="end":
        break
    participantes.append(entrada)

# Imprimir la informacion
print("Hay %s inscritos" % len(participantes))
for p in participantes:
    print(p)

# Ahora queremos poner calificaciones a todos
calificaciones = {}
for p in participantes:
    print("Cual es la calificacion de ",p,"?")
    cal = float(input())
    calificaciones.update({p:cal})
  
#Imprimimos la lista de calificaciones  
print(calificaciones)
    