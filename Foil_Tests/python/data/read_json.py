import pandas as pd
import openpyxl
import csv
from openpyxl import Workbook as wb
from csv_to_xlsx import csv_to_xlsx
from IPython import display

# Read json file
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