# Ejemplo de una clase 'Casa'
import random as rd

class Casa:
    def __init__(self,m2,valor,numerobanios,jardin,centrico):
        self.superficie = m2
        self.valor      = valor
        self.banios = numerobanios 
        self.jardin     = jardin
        self.centrico = centrico
        self.valor_inicial = valor
    
    #Metodo para imprimir en la consola la informacion actual
    def describir(self):
        print("Es una casa de %s m2 con un valor de %s MXN (valor inicial %s MXN)" % (self.superficie,self.valor,self.valor_inicial)) 
     
    # Metodo que reduce el valor de la casa con una probablidad de 50% 
    def sismo(self):
        #Perdemos con 50% de probabilidad un 25% del valor
        if rd.uniform(0,1) > 0.5:
            self.valor *=0.75
            
           
   
casa1 = Casa(100,8000000,3,True,True)  #Creamos una nueva casa
print(type(casa1))      # Describimos el tipo de datos
casa1.describir()       # Describimos la casa
casa1.sismo()           # Devaluamos la casa con cierta probabilidad
casa1.describir()       # Describimos la casa
print("--------------------------------------------------------------")

# Ahora lo hacemos para 10 casa....
casas = []  # generamos una lista donde vamos a meter todas las casas
for i in range(0,10): #hacemo un ciclo para generar 10 casa (las metemos a casas)
    casas.append(Casa(rd.randint(60,130),rd.randint(100000,8000000),rd.randint(1,4),rd.choice([True,False]),(rd.uniform(0,1)>0.8)))
    
# Ahora podemos hacer un loop de todas las casas    
for c in casas: 
    c.describir()
    c.sismo()
    c.describir()
    print("Voy a la siguiente casa...\n ")
    
    
# SELECCIONAR ALEATORIAMENTE UNA CASA (de las 10)
# BUSCAR LA CASA (De las otras 9) que tiene el valor mas cercano a la casa seleccionada
print("------------------------")
miCasa = rd.choice(casas)       # Seleccionamos aleatoriamente una de las casas
miCasa.describir()              # Dejo que se describe (para saber cual es)
minDiff = 999999999999999       # Iniciamos una variable para encontrar la diferencia (ponemos un valor muy alto)
casaMasCercana = "n/a"          # Iniciamos la variable 'casaMasCercana'

for c in casas: # Ahora hacemos un ciclo para encontrar todas las casas
    # Usamos una doble condicion: queremos que la diferencia sea menos de la que mejor que encontramos hasta ahora
    # Pero al mismo tiempo mayor a 0 para no encontrar otra vez la misma casa
    if abs(c.valor-miCasa.valor) < minDiff and abs(c.valor - miCasa.valor) > 0:
        minDiff = abs(c.valor-miCasa.valor)  # Guardamos el nuevo mejor resultado
        casaMasCercana = c                  #Guardamos cual es la casa mas cercana (actual)

# Una vez que concluimos el ciclo, la variable 'casaMasCercana' apunta a la casa mas cercana
print("La casa con el valor mas cercano es:")
casaMasCercana.describir() #Simplemente dejamos que se describe

# Para controlar, pongo aqui todos los valores
for c in casas: 
    print("%12.2f" % c.valor)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

