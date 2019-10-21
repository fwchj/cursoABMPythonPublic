# -*- coding: utf-8 -*-

#Very simple mesa-model with N agents and a capital increasing by 5% in each period (single file model)
from mesa import Agent,Model
from mesa.time import RandomActivation


class miAgente(Agent):  #Definimos la clase
    
    # Constructor
    def __init__(self,unique_id,model,capital):
        super().__init__(unique_id, model)
        self.capital = capital
    # Metodo step (nada mas imprime algo)
    def step(self):
        self.capital = 1.05*self.capital
        print("Soy el agentes %s y mi capital es %5.3f" % (self.unique_id,self.capital))
        
        
class miModelo(Model):
    def __init__(self,N_agentes):
        self.schedule = RandomActivation(self)

        for i in range(0,N_agentes):
            a = miAgente(i,self,self.random.randrange(5,15))
            self.schedule.add(a)
            
    def step(self):
        self.schedule.step()  
        print("---- End of tick ----")     
      

modelo1 = miModelo(10)  # Generamos un modelo con 10 agentes
modelo1.step()
modelo1.step()
