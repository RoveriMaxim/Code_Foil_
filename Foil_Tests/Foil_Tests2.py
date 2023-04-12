import pandas as pd
import openpyxl
import csv
from openpyxl import Workbook as wb
from csv_to_xlsx import csv_to_xlsx
from IPython import display

file = pd.read_excel('data_.xlsx')
print("\n", "________________________________________________________________________", " File Columns ", "________________________________________________________________________")
print(file.columns)

print("\n", "________________________________________________________________________", " File iloc ", "________________________________________________________________________", "\n")

print(file.iloc[0:5, 0:5])
print("")

