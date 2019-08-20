import csv
print("---------------------EJEMPLO 1----------------------")
# Separado por , y queremos convertirlo a lista
with open('workers.txt','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
csvFile.close()   
   
print("---------------------EJEMPLO 2----------------------")
# Separado por ; y queremos convertir a dictionario
csv.register_dialect('myDialect', delimiter = ';')        
with open('workers_semicolor.txt','r') as csvFile:
    reader = csv.DictReader(csvFile, dialect="myDialect")
    for row in reader:
        print(row)
        
csvFile.close()

