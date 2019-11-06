# -*- coding: utf-8 -*-
#server.py: setup of the server
from mesa.visualization.ModularVisualization import  ModularServer
from mesa.visualization.modules import CanvasGrid,ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from FoodModel import FoodModel,FoodAgent,Food

# Define the layout/design of the agents. Given that we have two here, we need an if-else       
def food_portrayal(agent):
    
    portrayal = {}
    if type(agent) is Food:
        colors = ["#FFFFFF","#E3EEE5","#C7DECB","#ACCEB2","#90BE98","#75AE7E","#599E65","#3E8E4B","#227E31","#076E18"]
        color=colors[agent.energy]
        portrayal = {"Shape":"rect",
            "Color":color,
            "Filled":"true",
            "Layer":0,
            "w":1,
            "h":1}
    elif type(agent) is FoodAgent:
        
        portrayal = {"Shape":"circle",
            "Color":"red",
            "Filled":"true",
            "Layer":5,
            "r":0.5}
    return portrayal

# Setup the parameters: here changeable by the user
model_params = {"N": UserSettableParameter('slider',"Number of agents",1,1,8,1)}

# Setup the visualisation of the grid
canvas_element = CanvasGrid(food_portrayal, 20,20, 500, 500)

# Define two charts (based on the collected data!)
chart = ChartModule([{"Label":"Collected energy","Color":"red"},{"Label":"Active agents","Color":"blue"}],data_collector_name='datacollector')
chart2 = ChartModule([{"Label":"Active agents","Color":"blue"}],data_collector_name='datacollector')

# Combine all and setup the server
server = ModularServer(FoodModel, [canvas_element,chart,chart2], "Food model", model_params)
 
# Note, executing this file will NOT start the server. Please to to runServer.py










