from model import miModelo
from mesa.batchrunner import BatchRunner 
from EjemplosClase.mesa.ejemplo2.model import contarAgentes
import matplotlib.pyplot as plt

fixed_params ={}
variable_params = {"N": range(4,15,1),"seed":range(0,10)}

batchRun = BatchRunner(miModelo,
                       fixed_parameters=fixed_params,
                       variable_parameters= variable_params,
                       iterations=1,
                       max_steps=5000,
                       model_reporters={"numTicks":contarAgentes})

batchRun.run_all()

batch_data = batchRun.get_model_vars_dataframe()

print(batch_data)

plt.scatter(batch_data.N,batch_data.numTicks)
plt.show()