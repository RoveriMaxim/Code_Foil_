import pandas as pd
import openpyxl
import csv
from IPython import display
from arpeggio import ParserPython
from openpyxl import Workbook as wb
from arpeggio import visit_parse_tree

from methods import append_once, list_int64_toString
from foil.language.grammar import comment


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataframe = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\F004-Carriere(150322).xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
# datamedia contiene tutte le righe (eccetto quelle null) di tutte le colonne 
data_media = dataframe[~dataframe["MEDIA P"].isna()]


indice = data_media.iloc[:, 0]
matricole = []
for k in range(len(indice)):
    matricole.append(indice.iloc[k]) # Creo una lista di matricole (int64)
for i in range(len(matricole)):
    matricole[i] = str(matricole[i]) # Converto le matricole in stringhe (object)


indice = data_media.iloc[:, 25]
ad_des = []
for k in range(len(indice)):
    ad_des.append(indice.iloc[k])# Creo una lista di _esami _sostenuti dagli
                                                # _alunni + matricole(object)


indice = data_media.iloc[:, 19]
ic_fc = []
for k in range(len(indice)):
    ic_fc.append(indice.iloc[k])# Creo una lista di alunni _in corso
                                # e _fuori corso  + _matricole(object)


# Aggiungo il predicato s alle matricole
matricole = list(map(str, matricole))
for k in range(len(matricole)):
    matricole[k] = "(s" + matricole[k] + ")."


indice = data_media.iloc[:, 7]
bool_worker = []
for k in range(len(indice)):
    if "non lavoratore: tempo studio > 75%" or "Non occupato-Iscrito full time" in str(indice.iloc[k]):
        bool_worker.append(matricole[k] + " " + "non_lavoratore")# lista studenti non lavoratori
    elif "lavoratore: tempo studio < 75%" in str(indice.iloc[k]):
        bool_worker.append(matricole[k] + " " + "lavoratore")# lista studenti lavoratori


l_voti = data_media.iloc[:, 30] # salvo in range_voti[] i voti di laurea dei vari stuenti con le relative matricole
range_voti = []
l_voti = [0 if str(x) == "nan" else x for x in l_voti]
for k in range(len(l_voti)):
    if (18 <= l_voti[k] <= 25  and  ad_des[k] == "ALGORITMI E STRUTTURE DATI"):
        range_voti.append(matricole[k] + " " + "a_18_25")
    elif (26 <= l_voti[k] <= 30  and  ad_des[k] == "ALGORITMI E STRUTTURE DATI"):
        range_voti.append(matricole[k] + " " + "a_26_30")

    elif (18 <= l_voti[k] <= 25  and  ad_des[k] == "FONDAMENTI DI SICUREZZA"):
        range_voti.append(matricole[k] + " " + "f_18_25")
    elif (26 <= l_voti[k] <= 30  and  ad_des[k] == "FONDAMENTI DI SICUREZZA"):
        range_voti.append(matricole[k] + " " + "f_26_30")

    elif (18 <= l_voti[k] <= 25  and  ad_des[k] == "ALGEBRA E GEOMETRIA"):
        range_voti.append(matricole[k] + " " + "g_18_25")
    elif (26 <= l_voti[k] <= 30  and  ad_des[k] == "ALGEBRA E GEOMETRIA"):
        range_voti.append(matricole[k] + " " + "g_26_30")


# Lode:  833
# Non lode:  32629
indice = data_media.iloc[:, 22]
lode_esame = []
for k in range(len(indice)):
    if "L" in str(indice.iloc[k]):
        lode_esame.append(matricole[k] + " " + "lode")
    else:
        lode_esame.append(matricole[k] + " " + "non_lode")


