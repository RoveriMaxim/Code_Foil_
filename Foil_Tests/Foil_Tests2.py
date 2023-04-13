import pandas as pd
import openpyxl
import csv
from openpyxl import Workbook as wb
from Methods import append_once
from IPython import display


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataframe = pd.read_excel('F004-Carriere(150322).xlsx')
new_data = dataframe[~dataframe["MATRICOLA"].isna()]

indice = new_data.iloc[:, 0]
matricole = []
students_matr = []

for k in range(len(indice)):
    matricole.append(indice.iloc[k])
students_matr = append_once(matricole)
# print("\n", students_matr, "\n")














""" print("\n", "________________________________________________________________________", " File Columns ", "________________________________________________________________________")
print(file.columns)
 """

""" print("\n", "________________________________________________________________________", " File iloc _0:5, 0:2_", "________________________________________________________________________", "\n")
print(file.iloc[0:5, 0:2])
print("")

print("\n", "________________________________________________________________________", " Data File isna", "________________________________________________________________________", "\n")

data_file = file.isna() """