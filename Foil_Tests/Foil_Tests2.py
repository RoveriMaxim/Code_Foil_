import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Carica i dati di addestramento
train_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.train'
train_data = pd.read_csv(train_url, header=None, prefix='F')

# Carica i dati di test
test_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.test'
test_data = pd.read_csv(test_url, header=None, prefix='F')


# Unisci i dati di addestramento e di test in un unico dataset
data = pd.concat([train_data, test_data])

# Assegna i nomi alle colonne del dataset
# columns = ['OVERALL_DIAGNOSIS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
#           'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22'] 
columns = ['OVERALL_DIAGNOSIS']# + ['F{}'.format(i) for i in range(1, 23)]

for i in range(1, 23):
    columns.append("F{}".format(i)+"R")
    columns.append("F{}".format(i)+"S")
data.columns = columns
print(data)

# Visualizza le prime 10 righe del dataset
# print(data.head(10))
print(data)



""" jsfile = open('C:/Users/user/.vscode/Code_Foil_/Foil_Tests/datapackage.json', 'r')

# Parse
obj = json.loads(jsfile.read())


print(obj.get('resources')[0].get('name'))

# Da qui in poi gestiamo l'oggetto json creato potendoci interagire
list = obj['resources']


# print("LE CHIAVI: ", keys)

for i in range(len(list)):
    print("\n\n")
    print("list i: ", list[i])
    print("\n")
    keys = list[i].keys()
    for k, key in enumerate(keys):
        print("Dato__ ", k,": ",key, "il valore del dato e': ", list[i].get(key))

print("\n\n") """
