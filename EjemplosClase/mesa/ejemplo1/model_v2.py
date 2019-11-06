from mesa import Agent,Model
from mesa.time import BaseScheduler,RandomActivation
from mesa.datacollection import DataCollector

class Persona(Agent):
    def __init__(self,unique_id,model,nombre,dinero):
        super().__init__(unique_id,model) #llamamos a la superclase (constructor)
        self.nombre = nombre    # definimos y asignamos una variable de instancia nombre
        self.dinero = dinero    # definimos y asignamos una variable de instancia dinero
        
    def step(self):
        if self.dinero > 0:
            mi_amigo = self.model.random.choice(self.model.schedule.agents)
            print("%s(%s) da 1 peso a %s(%s)" % (self.nombre,self.unique_id,mi_amigo.nombre,mi_amigo.unique_id))
            self.dinero -=1     # Quitamos un peso al agente activo
            mi_amigo.dinero +=1 # Agregamos un peso al amigo
            
        
def countAgentWithPositiveBalance(model):
    counter = 0
    for a in model.schedule.agents:
        if a.dinero > 0: 
            counter += 1
    return counter

class Amigo(Model):
    def __init__(self,numero_agentes):
        self.schedule =  RandomActivation(self)
        self.current_id = 0
        nombres =["Edgar","Sofia","Diana","Brenda","Alejandra","Alberto","Alex","Martin","Juan","Marta","Laura","Pedro"]
        for i in range(0,numero_agentes):
            a = Persona(self.next_id(),self,self.random.choice(nombres),5)
            self.schedule.add(a)
        
        self.datacollector = DataCollector(
            agent_reporters={"Dinero":"dinero","Nombre":"nombre"},
            model_reporters={"AgentWithMoney":countAgentWithPositiveBalance})
        
    def step(self):
        self.schedule.step()
        for a in self.schedule.agents:
            print(" %s(%s) ahora tiene %s pesos" % (a.nombre,a.unique_id,a.dinero))
        self.datacollector.collect(self)
        print("--- Fin de tick ---")
        


m2 = Amigo(4)

for i in range(0,5):
    m2.step()

print("=== RESULTADO FINAL ====")
for a in m2.schedule.agents:
    print("%s tiene %s pesos" % (a.nombre,a.dinero))
print(m2.datacollector.get_agent_vars_dataframe())
print("---------")
print(m2.datacollector.get_model_vars_dataframe())














