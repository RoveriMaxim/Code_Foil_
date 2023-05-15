import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import csv
from IPython import display
from arpeggio import ParserPython
from openpyxl import Workbook as wb
from arpeggio import visit_parse_tree

from models import Clause, Example, Label
from methods import crea_dizionario


# imposto il numero massimo di righe e colonne visualizzate su None, che significa "nessun limite"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# leggo il file excel
# converto la colonna MATRICOLA in stringa
# datamedia contiene tutte le righe (eccetto quelle null) di tutte le colonne
dataframe = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\F004-Carriere(150322).xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
data_media = dataframe[~dataframe["MEDIA P"].isna()]


# Creo due liste matricole, una con le matricole e una con le matricole e il predicato s
# Converto le matricole in stringhe (object)
# Creo poi una lista con le matricole senza duplicati
indice = data_media.iloc[:, 0]
matricole = []
matricole_2 = []
for k in range(len(indice)):
    matricole.append(indice.iloc[k])
    matricole_2.append(indice.iloc[k])
for i in range(len(matricole)):
    matricole[i] = str(matricole[i])
    matricole_2[i] = str(matricole_2[i])

matricole = list(map(str, matricole))
for k in range(len(matricole)):
    matricole[k] = "(s" + matricole[k] + ")."

matr_no_dupl = dataframe.drop_duplicates(subset=['MATRICOLA'])


# Lista studente lavoratore o non lavoratore
lav_no_lav = []
for index, distinct_row in matr_no_dupl.iterrows():
    if "Non occupato-Iscrito full time" or "Non occupato-Iscritto part time" in str(distinct_row[7]):
        lav_no_lav.append("non_occup_(s" + distinct_row[0]+").")

    elif "Occupato-Iscritto full Time" in str(distinct_row[7]) or "Occupato-Iscritto part time" in str(distinct_row[7]):
        lav_no_lav.append("occup_(s" + distinct_row[0]+").")

    elif "lavoratore-studente: tempo studio < 50%" in str(distinct_row[7]) or "studente-lavoratore: tempo studio 50%75%" in str(distinct_row[7]):
        lav_no_lav.append("stud_lav_(s" + distinct_row[0]+").")

    elif "non lavoratore: tempo studio > 75%" == str(distinct_row[7]):
        lav_no_lav.append("non_lav_gr75_(s" + distinct_row[0]+").")
        
    elif "Non fornito-Iscritto full time" == str(distinct_row[7]):
        lav_no_lav.append("nan_fulltime_(s" + distinct_row[0]+").")


# Lista studenti fuori corso o non fuori corso
ic_fc = []
for index, matr in matr_no_dupl.iterrows():
    if "IC" in str(matr[19]):
        ic_fc.append("in_corso" + "(s" + matr[0] + ").")
    else:
        ic_fc.append("fuori_corso" + "(s" + matr[0] + ").")



# Lista delle medie ponderate suddivise per range
range_medie_matr = []
for index, medie in matr_no_dupl.iterrows():
    if(str(medie[34]) != "nan"):
        if(18 <= medie[34] <= 20):
            range_medie_matr.append("m_18_20_" + "(s" + medie[0] + ").")
        elif(21 <= medie[34] <= 24 ):
            range_medie_matr.append("m_21_24_" + "(s" + medie[0] + ").")
        elif(25 <= medie[34] <= 27):
            range_medie_matr.append("m_25_27_" + "(s" + medie[0] + ").")
        elif(28 <= medie[34] <= 30):
            range_medie_matr.append("m_28_30_" + "(s" + medie[0] + ").")
    else:
        range_medie_matr.append("esami_sostenuti_insufficienti" + "(s" + medie[0] + ").")


# OK
# Lista degli esami suddivisi per range di voto
range_voti_esami = []
for index, row in data_media.iterrows():
    mat = "(s"+row[0]+")."
    if (18 <= row[30] <= 25  and  row[25] == "PROGRAMMAZIONE"):
        range_voti_esami.append("p_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "PROGRAMMAZIONE"):
        range_voti_esami.append("p_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "ALGORITMI E STRUTTURE DATI"):
        range_voti_esami.append("a_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "ALGORITMI E STRUTTURE DATI"):
        range_voti_esami.append("a_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "BASI DI DATI"):
        range_voti_esami.append("b_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "BASI DI DATI"):
        range_voti_esami.append("b_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "RETI DI TELECOMUNICAZIONE"):
        range_voti_esami.append("r_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "RETI DI TELECOMUNICAZIONE"):
        range_voti_esami.append("r_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "INGLESE"):
        range_voti_esami.append("i_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "INGLESE"):
        range_voti_esami.append("i_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "LOGICA"):
        range_voti_esami.append("l_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "LOGICA"):
        range_voti_esami.append("l_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "FONDAMENTI DI SICUREZZA"):
        range_voti_esami.append("f_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "FONDAMENTI DI SICUREZZA"):
        range_voti_esami.append("f_26_30" + mat)

    elif (18 <= row[30] <= 25  and  row[25] == "LABORATORIO INTERDISCIPLINARE B"):
        range_voti_esami.append("lib_18_25" + mat)
    elif (26 <= row[30] <= 30  and  row[25] == "LABORATORIO INTERDISCIPLINARE B"):
        range_voti_esami.append("lib_26_30" + mat)

  
# PROVA
gruppi = dataframe.groupby('MATRICOLA')
# crea una lista degli esami per ogni matricola
lista_esami = gruppi['AD_COD'].unique()
# conta il numero di esami superati per ogni matricola
conteggio_esami = dataframe['MATRICOLA'].value_counts()
# FINE PROVA

"""
lav_no_lav              lista degli studenti lavoratori e non
ic_fc                   lista degli studenti in corso e fuori corso (?)
range_voti_esami        lista degli esami sostenuti con il relativo range di voti
range_medie_matr        lista delle medie ponderate suddivise per range 
"""

insieme = lav_no_lav + ic_fc + range_medie_matr + range_voti_esami


def il_back():
    background = []
    dati = insieme
    for k in range(len(dati)):
        background.append(Clause.parse(str(dati[k])))
    return background


def gli_es():
    positivi = []
    negativi = []

    # TODO - differenzia
    elite = dataframe.loc[dataframe["VOTO_LAUREA"] == 110]
    # elite = dataframe.loc[dataframe["LODE_LAU"] == "L"]
    elite_mat = elite.iloc[:, 0].drop_duplicates()

    non_elite = dataframe.loc[(dataframe["VOTO_LAUREA"] != 110) & (~dataframe["VOTO_LAUREA"].isna())]
    non_elite_mat = non_elite.iloc[:, 0].drop_duplicates().to_list()
    # mappo a str la lista non_elite_mat
    non_elite_mat = list(map(str, non_elite_mat))


    # Viene crato un oggetto "Example". 
    # Esso viene inizializzato con un dizionario che ha una chiave 'X' e un valore che combina
    # la stringa "s" con il valore della riga corrispondente in elite_mat
    # (ottenuto tramite elite_mat.iloc[k].
    # L'etichetta dell'oggetto Example viene impostata su Label.POSITIVE. 
    # Infine, l'oggetto Example viene aggiunto all'elenco positivi.
    for k in range(len(elite_mat)):
        positivi.append(Example({'X': "s" + str(elite_mat.iloc[k])}, Label.POSITIVE))
    for k in range(len(non_elite_mat)):
        negativi.append(Example({'X': "s" + str(non_elite_mat[k])}, Label.NEGATIVE))

    totale = positivi + negativi

    return totale
