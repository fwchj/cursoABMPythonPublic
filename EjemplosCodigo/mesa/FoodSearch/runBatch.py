# -*- coding: utf-8 -*-
#runBatch.py: prepares and executes the batch run
from FoodModel import FoodModel,Agent,Food,sumEnergy
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt

# Define the parameters (here we only have variable parameters)
fixed_params    ={}
variable_params = {"N":range(1,9,1)}

# Setup the batch-run
batch_run = BatchRunner(FoodModel,                              # Model selection
                        fixed_parameters=fixed_params,          # Select fixed parameters
                        variable_parameters=variable_params,    # Select variable parameters
                        iterations=25,                          # How many identical runs?
                        max_steps=1000, #Max number of ticks (to avoid never-ending-runs)
                        model_reporters={"Energy":sumEnergy}) #Indicate what information to collect

batch_run.run_all() #Actually execute the batch run

# post-simulation: use of the data (standard python programming)
run_data = batch_run.get_model_vars_dataframe()
print(run_data.head())
print(run_data)

plt.scatter(run_data.N,run_data.Energy)
plt.show()