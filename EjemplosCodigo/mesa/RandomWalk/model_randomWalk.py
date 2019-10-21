from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class Persona(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id, model)
    def step(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos,moore=True)
        target = self.model.random.choice(neighborhood)
        self.model.grid.move_agent(self,target)
        print("Ahora estoy en ",self.pos)
       
class RWModel(Model):
    def __init__(self):
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10,10,True)
        self.running = True
        
        #Add agent
        agent = Persona(1,self)
        self.schedule.add(agent)
        self.grid.place_agent(agent, (5,5))
        
    def step(self):
        self.schedule.step()

        
myModel = RWModel()
myModel.step()
