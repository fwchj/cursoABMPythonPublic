'''
This file allows you to run the model in batch mode (e.g. many times) and analyse the 
data of all batch runs at the end
'''
from food_model import *
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt


# Here we define all the variables that will be equal for each run
fixed_params = {
    "width": 10,
    "height": 10,
    "N" : 50,
    "energyConsumption": 1,
    "energyGain": 5,
}

# Let us now define the variables that change from simualtion to simulation
variable_params = {"Nfood": range(1,11)}

# The variables parameters will be invoke along with the fixed parameters allowing for either or both to be honored.
batch_run = BatchRunner(
    Food_model,  #Select the correct model (previously imported)
    variable_params,
    fixed_params,
    iterations=5,   # How many times to simulate each setting
    max_steps=100,  # After how many periods the model should stop? 
    model_reporters={"Bugcounter": countBugs} #What information should we get from the model (only for last period)
)

#Run the model in batch mode
batch_run.run_all()                                 

# Once the run is over, get the data from the model and plot interesting stuff
run_data = batch_run.get_model_vars_dataframe()
print(run_data.head())
plt.scatter(run_data.Nfood, run_data.Bugcounter)
plt.show()
