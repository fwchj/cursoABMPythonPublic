from model import miModelo
from mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


def portrayal(agent):
    
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "Color": "black",
                 "text": agent.unique_id,
                 "text_color": "white",
                 "r":0.75}
    return portrayal

grid = CanvasGrid(portrayal,10,10,500,500)
chart = ChartModule([{"Label":"Nagentes","Color":"red"}],data_collector_name="datacollector")

server = ModularServer(miModelo,
                       [grid,chart],
                       "Nuestro segundo modelo",
                       {"N":UserSettableParameter('slider',"Numero de agentes",5,1,50,1)})  