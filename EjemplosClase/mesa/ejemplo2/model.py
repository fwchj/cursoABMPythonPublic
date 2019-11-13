from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector


class miAgente(Agent):
    def __init__(self,unique_id,model,value):
        super().__init__(unique_id, model)
        self.value = value
        colores = ["red","blue","green","yellow","black"]
        self.color = self.model.random.choice(colores)
    
    def step(self):
        vecindad = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        destino = self.random.choice(vecindad)
        self.model.grid.move_agent(self,destino)
        
        # Vemos ahora si hay dos
        vecinos = self.model.grid.get_neighbors(self.pos,moore=True, include_center=True,radius=0)
        
        # vesion sencialla. if len(vecinos) > 1: 
        
        # version mas correcta
        vecinos = [x for x in vecinos if type(x) is miAgente and x!=self]
        if len(vecinos)>0: 
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
            for v in vecinos: 
                self.model.schedule.remove(v)
                self.model.grid.remove_agent(v)
                
def contarAgentes(model):
    return model.schedule.steps  

def getCurrentTick(model):
    return model.schedule.get_agent_count()      

class miModelo(Model):
    def __init__(self,N,seed=None):
        self.current_id=0
        self.running = True
        # Definimos el schedule para hacer la ejecucion en orden aleatorio
        self.schedule = RandomActivation(self)
        
        #Definimos el grid de tamanio 10x10 y sin fronteras flexibles
        self.grid = MultiGrid(10,10,False)
        
        for i in range(N):
            a = miAgente(self.next_id(),self,5)
            self.schedule.add(a)
            pos_x = self.random.randint(0,9)
            pos_y = self.random.randint(0,9)
            
            self.grid.place_agent(a, [pos_x,pos_y])
        
        self.datacollector = DataCollector(
            model_reporters={"Nagentes": contarAgentes,"NumberTicks":getCurrentTick})
        
        
    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        # Paramos la simulacion cuando hay menos de dos agentes
        if self.schedule.get_agent_count()<2:
            self.running = False
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        