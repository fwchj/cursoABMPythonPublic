# -*- coding: utf-8 -*-
# runSimple.py: manual run of model (essentially for testing)

#Import the model
from FoodModel import FoodModel

#Setup on instance of the model (with two agents)
myModel = FoodModel(2)


myModel.step() #execute one tick
myModel.step() #execute one tick
myModel.step() #execute one tick
myModel.step() #execute one tick
myModel.step() #execute one tick

# Get the data
data = myModel.datacollector.get_model_vars_dataframe()
print(data)