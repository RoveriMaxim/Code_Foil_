import csv
import pandas as pd
from openpyxl import Workbook
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3


# Read csv file and convert it to xlsx
def csv_to_xlsx(csv_file_input, xlsx_name_output):
    wb = Workbook()
    wba = wb.active
    with open(csv_file_input, 'r') as f:
        for row in csv.reader(f):
            wba.append(row)
            nuovo_file = wb.save(xlsx_name_output)
        print("\n", "________________________________________________________________________",
              "finito", "________________________________________________________________________", "\n")
        
    return nuovo_file


def append_once(list):
    x=0
    final_list = []

    for elem in list:
        if elem not in final_list:
            final_list.append(str(elem))
    return final_list


def list_int64_toString(list):
    i=0
    string = []
    for i in list:
        string.append(str(i))
    return string


def get_alpha3(col):
    try:
        iso_3 =  country_name_to_country_alpha3(col)
    except:
        iso_3 = 'Unknown'
    return iso_3

def get_name(col):
    try:
        name =  country_alpha2_to_country_name(col)
    except:
        name = 'Unknown'
    return name


def crea_dizionario(chiave, valore):
    dizionario = {}
    for i in range(len(chiave)):
        if chiave[i] not in dizionario:
            dizionario[chiave[i]] = valore[i]

 
""" # Returns a scalar
# titanic.ix[4, 'age']
titanic.at[4, 'age']

# Returns a Series of name 'age', and the age values associated
# to the index labels 4 and 5
# titanic.ix[[4, 5], 'age']
titanic.loc[[4, 5], 'age']

# Returns a Series of name '4', and the age and fare values
# associated to that row.
# titanic.ix[4, ['age', 'fare']]
titanic.loc[4, ['age', 'fare']]

# Returns a DataFrame with rows 4 and 5, and columns 'age' and 'fare'
# titanic.ix[[4, 5], ['age', 'fare']]
titanic.loc[[4, 5], ['age', 'fare']]
 """
 
"""def is_old_func(row):
    return row['age'] > 60
titanic['is_old'] = titanic.apply(is_old_func, axis='columns')
 """


# Read csv file and convert it to xlsx
""" df = pd.read_csv('U.S._Chronic_Disease_Indicators.csv', sep=',', header=0, low_memory=False, chunksize=1000)

def csv_to_xlsx(csv_file, xlsx_file):
    ws = wb.active
    with open(csv_file, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
            nuovo_file = wb.save(xlsx_file)
    return nuovo_file

csv_to_xlsx('U.S._Chronic_Disease_Indicators.csv', 'U.S._Chronic_Disease_Indicators.xlsx')

print("finito") """

# Read csv file
""" df = pd.read_csv('U.S._Chronic_Disease_Indicators.csv', sep=',', header=0, low_memory=False, chunksize=100)

for chunk in df:
    categories = ['YearStart', 'YearEnd', 'LocationAbbr', 'LocationDesc', 'Topic', 'Question', 'DataValueUnit', 
                     'DataValueType', 'DataValue', 'DataValueAlt', 'DataValueFootnoteSymbol', 'DataValueFootnote', 
                     'LowConfidenceLimit', 'HighConfidenceLimit']
    details = chunk[categories]
    details ['DataValue'] = 1    # pd.to_numeric(details['DataValue'], errors='coerce')
    summary = details.groupby(categories).sum().reset_index()
    # display(details.head())
    display(summary.head())

    break """