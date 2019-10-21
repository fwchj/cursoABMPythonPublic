''' 
This file contains the whole model (definition of agents and the model), but is not executable. Depending on how you want 
to run the model, you will need to use other files: 
- single run in the browser: use run.py
- batch run for statistical analysis: use batchRun.py
''' 
from mesa import Agent,Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace
from mesa.datacollection import DataCollector


def countBugs(model):
    ''' This method counts the number of bugs present in the model '''
    agents = [x for x in model.schedule.agents if type(x) is Bug]
    return len(agents)

class Bug(Agent):
    ''' Here we define the class Bug, which is one of our key agents'''
    def __init__(self,unique_id,model):
        ''' The constructor is used to create the Bug'''
        super().__init__(unique_id, model)
        self.energy =   10  # We always start with energy=10
        
    
    def move_towards(self,target,maxDistance=1):
        ''' This is a method to move an agent (bug) towards another object
            target: object towards which the bug wants to move (typically Food!)
            maxDistance: the maximum distance the bug can move. If target closer, only the bug only moves required distance.
        ''' 
        dist = self.model.space.get_distance(self.pos,target.pos) # Compute the distance between the two
        
        if dist <= maxDistance: #If the distance is less than the max, the bug just goes to the target
            self.model.space.move_agent(self,target.pos)
        else: #Otherwise, we have to compute the point where the bug can go
            x1,y1 = self.pos[0],self.pos[1]
            x2,y2 = target.pos[0],target.pos[1]
            xt = x1 + (x2-x1)*(maxDistance/dist)
            yt = y1 + (y2-y1)*(maxDistance/dist)
            self.model.space.move_agent(self,(xt,yt))
            
        
        
        
    def findFood(self):
        ''' This method allows bugs to find the closest piece of food '''
        
        #Search the space for all agents and the filter for Food
        candidates = self.model.space.get_neighbors(self.pos,radius=500,include_center=False)
        candidates = [x for x in candidates if type(x) is Food]
        
        # Define temporary variable in which we will store the best match
        best = None
        min_dist = 9999999999999 #Start with a very high value which is always higher than the actual distances
        
        # Loop over all candidates and see which one is the nearest
        for c in candidates:
            thisDist = self.model.space.get_distance(self.pos,c.pos)
            if type(c) is Food and thisDist < min_dist:
                #print("Distance: ",thisDist)
                best = c
                min_dist = thisDist
                
        # If and only if a close food was found, move towards it (max distance = 1)            
        if best is not None:
            self.move_towards(best,1)                   # move
            self.energy-= self.model.energyConsumption  # Reduce energy by the amount needed to move
            
            # Check if bug dies (if energy below 0)
            if self.energy<=0:
                self.model.schedule.remove(self)
                
            # Check if the bug reached Food (if yes, eat it)    
            candidates = self.model.space.get_neighbors(self.pos,radius=0,include_center=True)
            candidates = [x for x in candidates if type(x) is Food]
            if len(candidates) >0: # If there is food, the length should be >0
                for l in candidates: # Each each piece of food (typically only one)
                    self.energy +=self.model.energyGain
                    
                    # Now let us move the food (it's like if a new food appears somewhere else
                    x = self.model.random.random() * (self.model.space.x_max)
                    y = self.model.random.random() * (self.model.space.y_max)
                    self.model.space.move_agent(l,(x,y))

                # Once all food is consume, let's check if the bug procreates (divides into to)
                if self.energy>30:  
                    self.energy /=2     # Divide the energy by 2
                    newAgent = Bug(self.model.next_id(),self.model) # Generate a new bug
                    newAgent.energy = self.energy                   # Give half of the energy to the new bug
                    newAgent.pos=(0,0)          # Initiate the variable pos        
                    self.model.schedule.add(newAgent)   # Add the bug to the scheduler
                    # Find random coordinates where to place the bug
                    x = self.model.random.random() * (self.model.space.x_max)
                    y = self.model.random.random() * (self.model.space.y_max)
                    self.model.space.place_agent(newAgent,(x,y))
    
    def step(self):
        ''' this method is called by the scheduler in each period '''
        self.findFood()

class Food(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id, model)


        
class Food_model(Model):
    
    def __init__(self,N,width,height,energyConsumption,Nfood,energyGain):
        self.space = ContinuousSpace(width,height,False)
        self.Nagents = N
        self.Nfood = Nfood
        self.schedule = RandomActivation(self)
        self.energyConsumption = energyConsumption
        self.energyGain = energyGain
        self.running = True
        self.current_id = 1
        self.tick = 0
        
        
        # Define the worms
        for i in range(self.Nagents):
            a = Bug(self.next_id(),self)
            self.schedule.add(a)       

            x = self.random.random() * (self.space.x_max)
            y = self.random.randrange(self.space.y_max)
            self.space.place_agent(a,(x,y))
                   
        # Add some food 
        for i in range(Nfood):
            f = Food(self.next_id(),self)
            self.schedule.add(f)
            x = self.random.randrange(self.space.x_max)
            y = self.random.randrange(self.space.y_max)
            self.space.place_agent(f,(x,y))
            
        self.datacollector = DataCollector(
            model_reporters={"Bugcounter":countBugs})
    def step(self):
        #self.datacollector.collect(self)
        self.schedule.step()                # Call the step function of the agents
        self.datacollector.collect(self)    # Collect data of the model
        agents = [x for x in self.schedule.agents if type(x) is Bug]  # Get a list of all Bugs
        self.tick +=1       # Increase the tick counter by 1
        if len(agents)==0 or self.tick>=250:    # Stop the model if reaching 250 ticks of running out of bugs
            self.running = False
        
        
             

