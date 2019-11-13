from model import miModelo

m1 = miModelo(30,seed=1)
for i in range(0,3):
    m1.step()

print(m1.datacollector.get_model_vars_dataframe())

m2 = miModelo(30,seed=1)
for i in range(0,3):
    m2.step()

print(m2.datacollector.get_model_vars_dataframe())