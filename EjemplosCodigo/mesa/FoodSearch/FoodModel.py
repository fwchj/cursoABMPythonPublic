# -*- coding: utf-8 -*-
#FoodModel.py: implements the agents and the model
from mesa import Agent,Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

# DEFINE AGENT TYPE 'FoodAgent': this is the animal searching for food
class FoodAgent(Agent):
    # Initialiser (requires unique_id and model for superclass
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)   # Initialise the super-class
        self.energy = 0         # Set energy to zero (start value)
        self.running = True     # This is a auxiliary attribute to see whether the agent still moves
    
    # The method step is the one that executes in each period 
    def step(self):
        # Find the neighbourhood: moore refers to the 8-neighbours
      
        #-------- INICIO -------
        vecinos = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)
        sum = 0
        for v in vecinos:
            sum += v.energy
        print("El promedio es:",sum/len(vecinos)) 
        #-------- FIN    -------
            
        neighborhood = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        
        # Find the best place to go (highest energy). 
        best =[0,0]
        for t in neighborhood:
            # Compute the energy
            cellmates = self.model.grid.get_cell_list_contents(t)
            energy = 0
            for c in cellmates:
                if type(c) is Food: 
                    energy += c.energy
            if energy > best[1]:
                best = [t,energy]
        
        # If there is a best place to go, move there and consume. Otherwise stay and set running to FALSE
        if best[0]==0:
            self.running = False
        else:
            self.model.running = True
            self.model.grid.move_agent(self,best[0])
            cellmates = self.model.grid.get_cell_list_contents([self.pos])
            for c in cellmates:
                if type(c) is Food:
                    self.energy += c.energy
                    c.energy=0
        
       

# DEFINE AGENT TYPE 'Food': this is the food associated to a given patch
class Food(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.energy = self.random.randrange(10)

# Define a function we will need later in the model            
def sumEnergy(model):
        agents = model.schedule.agents
        energy_collected = 0
        energy_remaining = 0
        
        for a in agents:
            if type(a) is Food:
                energy_remaining += a.energy
            if type(a) is FoodAgent:
                energy_collected += a.energy
        return energy_collected  
    
# Define another function we will need in the class model    
def activeAgents(model): 
    counter = 0
    agents = model.schedule.agents
    for a in agents:
        if type(a) is FoodAgent and a.running==True:
            counter +=1
    return counter

# DEFINE THE CLASS FoodModel: here we put the whole model
class FoodModel(Model):
    
    # The initialisation refers to the initialisation of the whole model (including agents)
    def __init__(self,N):
        self.schedule = RandomActivation(self) # This implies that agents are selected in a random order each period
   
        # Define the grid and set some global values
        self.grid = MultiGrid(20,20,False)
        self.current_id=1
        self.running=True
        
        # Add energy (food) to grid
        for x in range(20):
            for y in range(20):
                f = Food(self.next_id(),self)
                self.grid.place_agent(f,(x,y))
                
        
        
        #Create all the agents
        self.num_agents = N
        for i in range(N):
            a = FoodAgent(self.next_id(),self)
            self.schedule.add(a)    # We have to add all agents to the scheduler (to have access)
            
            self.grid.place_agent(a, (10,10)) # We start by putting them all in the centre
          
        # Define which data is collected during the simulation  
        self.datacollector = DataCollector(
            model_reporters={"Collected energy":sumEnergy,"Active agents":activeAgents})
  
     
    # Define the action (by the model) in each tick    
    def step(self):     
        self.running = False #Set running to false. It will be changes to true if at least one agent is still moving
        self.schedule.step() # executes the step() function for all agents in the scheduler
        self.datacollector.collect(self) #Collects data
        
            
 
      