import openpyxl
from openpyxl import Workbook
import csv

# Read csv file and convert it to xlsx
def csv_to_xlsx(csv_file, xlsx_file):
    wb = Workbook()
    wba = wb.active
    with open(csv_file, 'r') as f:
        for row in csv.reader(f):
            wba.append(row)
            nuovo_file = wb.save(xlsx_file)
        print("\n", "________________________________________________________________________",
              "finito", "________________________________________________________________________", "\n")
        
    return nuovo_file

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