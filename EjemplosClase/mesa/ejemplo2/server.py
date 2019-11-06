from model import miModelo
from mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

def portrayal(agent):
    
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "Color": agent.color,
                 "r":0.75}
    return portrayal

grid = CanvasGrid(portrayal,10,10,500,500)

server = ModularServer(miModelo,
                       [grid],
                       "Nuestro segundo modelo",
                       {"N":UserSettableParameter('slider',"Numero de agentes",5,1,50,1)})  