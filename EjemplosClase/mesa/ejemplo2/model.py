from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid


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
        

class miModelo(Model):
    def __init__(self,N):
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
        
    def step(self):
        self.schedule.step()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        