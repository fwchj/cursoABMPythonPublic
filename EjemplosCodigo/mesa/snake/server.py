'''
This file allows to run the model on the server and with a visualisation 
in the web browser. This is NOT the batch run
'''
from mesa.visualization.ModularVisualization import ModularServer
from SimpleContinuousModule import SimpleCanvas
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule

from food_model import *


def agent_draw(agent):
    if agent is None:
        return 
    
    if type(agent) is Bug:
        return {"Shape":"circle","r":agent.energy,"Filled":"true","Color":"black"}
    else:
        return {"Shape":"rect","h":0.025,"w":0.025,"Filled":"true","Color":"green"}
    

canvas = SimpleCanvas(agent_draw,500,500)
chart = ChartModule([{"Label": "Bugcounter",
                      "Color": "Black"}],
                    data_collector_name='datacollector')
model_params = {"N": UserSettableParameter('slider','Number of bugs', 3, 1, 10),
                "energyConsumption": UserSettableParameter('slider','Energy consumption', 1, 1, 5),
                "Nfood": UserSettableParameter('slider','Number of leafs', 10, 1, 50),
                "energyGain": UserSettableParameter('slider','Energy gain', 5, 1, 10),
                "width":10,"height":10}

server = ModularServer(Food_model,
                       [canvas,chart],
                       "Snake Model",
                       model_params)
server.port = 8523 # The default
