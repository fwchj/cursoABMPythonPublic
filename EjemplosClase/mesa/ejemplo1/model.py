from mesa import Agent,Model
from mesa.time import BaseScheduler,RandomActivation

class Persona(Agent):
    def __init__(self,unique_id,model,nombre,dinero):
        super().__init__(unique_id,model) #llamamos a la superclase (constructor)
        self.nombre = nombre    # definimos y asignamos una variable de instancia nombre
        self.dinero = dinero    # definimos y asignamos una variable de instancia dinero
        
    def step(self):
        print("Hola, me llamo %s y mi ID es %s" % (self.nombre,self.unique_id) )
        
    

class Amigo(Model):
    def __init__(self,numero_agentes):
        self.schedule =  RandomActivation(self)
        self.current_id = 0
        nombres =["Edgar","Sofia","Diana","Brenda","Alejandra","Alberto","Alex","Martin"]
        for i in range(0,numero_agentes):
            a = Persona(self.next_id(),self,self.random.choice(nombres),5)
            self.schedule.add(a)
        
    def step(self):
        self.schedule.step()
        print("--- Fin de tick ---")
        

m1 = Amigo(3)
m2 = Amigo(4)
m1.step()
m2.step()
m2.step()
m1.step()
















