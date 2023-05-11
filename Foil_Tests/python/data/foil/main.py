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
dataframe = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\F004.xlsx')
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
indice = data_media.iloc[:, 7]
lav_no_lav = []
for k in range(len(indice)):
    if "non lavoratore: tempo studio > 75%" or "Non occupato-Iscrito full time" in str(indice.iloc[k]):
        lav_no_lav.append("nonLavoratore" + matricole[k])
    elif "lavoratore: tempo studio < 75%" in str(indice.iloc[k]):
        lav_no_lav.append("lavoratore" + matricole[k])


# Lista con lo stato dello studente
indice3 = data_media.iloc[:, 14]
stato_studente = []
for k in range(len(indice3)):
    if "Attivo" in str(indice3.iloc[k]):
        stato_studente.append("attivo" + matricole[k])
    elif "Cons. Titolo" in str(indice3.iloc[k]):
        stato_studente.append("tit_cons" + matricole[k])
    elif "Decadenza" in str(indice3.iloc[k]):
        stato_studente.append("decadenza" + matricole[k])
    elif "Rinuncia" in str(indice3.iloc[k]):
        stato_studente.append("rinunciatario" + matricole[k])
    else:
        stato_studente.append("trasf" + matricole[k])


# Lista studenti fuori corso o non fuori corso
ic_fc = []
for index, matr in matr_no_dupl.iterrows():
    if "IC" in str(matr[19]):
        ic_fc.append("in_corso" + "(s" + matr[0] + ").")
    else:
        ic_fc.append("fuori_corso" + "(s" + matr[0] + ").")


# Lista studenti laureati con 110 e non
lau_lode = []
for index, matr in matr_no_dupl.iterrows():
    if str(matr[21]) != "nan" or matr[21] > 99:
        if (matr[21] == 110 and matr[22] == "L" or matr[21] == 110):
            lau_lode.append("lau_con_lode" + "(s" + matr[0] + ").")
        elif matr[21] < 110:
            lau_lode.append("lau_normale" + "(s" + matr[0] + ").")


# TODO - serve?
# Lista esami di ciascuno studente
ad_des = data_media.iloc[:, 25]
lista_nomi_esami = []
for k in range(len(ad_des)):
    lista_nomi_esami.append(ad_des.iloc[k] + matricole[k])


# Lista degli esami suddivisi per range di voto
voto_esame = data_media.iloc[:, 30]
range_voti_esami = []
voto_esame = [0 if str(x) == "nan" else x for x in voto_esame]
for k in range(len(voto_esame)):
    if (18 <= voto_esame[k] <= 25  and  lista_nomi_esami[k] == "ALGORITMI E STRUTTURE DATI" + matricole[k]):
        range_voti_esami.append("a_18_25" + matricole[k])
    elif (26 <= voto_esame[k] <= 30  and  lista_nomi_esami[k] == "ALGORITMI E STRUTTURE DATI" + matricole[k]):
        range_voti_esami.append("a_26_30" + matricole[k])

    elif (18 <= voto_esame[k] <= 25  and  lista_nomi_esami[k] == "FONDAMENTI DI SICUREZZA" + matricole[k]):
        range_voti_esami.append("f_18_25" +  matricole[k])
    elif (26 <= voto_esame[k] <= 30  and  lista_nomi_esami[k] == "FONDAMENTI DI SICUREZZA" + matricole[k]):
        range_voti_esami.append("f_26_30" + matricole[k])

    elif (18 <= voto_esame[k] <= 25  and  lista_nomi_esami[k] == "ALGEBRA E GEOMETRIA" + matricole[k]):
        range_voti_esami.append("g_18_25" + matricole[k])
    elif (26 <= voto_esame[k] <= 30  and  lista_nomi_esami[k] == "ALGEBRA E GEOMETRIA" + matricole[k]):
        range_voti_esami.append("g_26_30" + matricole[k])


# Lista esami con lode e senza lode
indice = data_media.iloc[:, 31]
lode_exam = []
for k in range(len(indice)):
    if "L" in str(indice.iloc[k]):
        lode_exam.append("exam_lode" + matricole[k])
    else:
        lode_exam.append("exam_non_lode" + matricole[k])


# Lista delle medie ponderate suddivise per range
medie_matr_range = []
for index, medie in matr_no_dupl.iterrows():
    if(str(medie[34]) != "nan"):
        if(18 <= medie[34] <= 20):
            medie_matr_range.append("m_18_20_" + "(s" + medie[0] + ").")
        elif(21 <= medie[34] <= 24 ):
            medie_matr_range.append("m_21_24_" + "(s" + medie[0] + ").")
        elif(25 <= medie[34] <= 27):
            medie_matr_range.append("m_25_27_" + "(s" + medie[0] + ").")
        elif(28 <= medie[34] <= 30):
            medie_matr_range.append("m_28_30_" + "(s" + medie[0] + ").")
    else:
        medie_matr_range.append("esami_sostenuti_insufficienti" + "(s" + medie[0] + ").")

    
# PROVA
gruppi = dataframe.groupby('MATRICOLA')
# crea una lista degli esami per ogni matricola
lista_esami = gruppi['AD_COD'].unique()
# conta il numero di esami superati per ogni matricola
conteggio_esami = dataframe['MATRICOLA'].value_counts()
# FINE PROVA

"""
lav_no_lav              lista degli studenti lavoratori e non
stato_studente          lista dello status degli studenti
ic_fc                   lista degli studenti in corso e fuori corso (?)
lau_lode                lista degli studenti laureati con lode e senza lode
lista_nomi_esami        lista degli esami di caiscuno studente (?)
range_voti_esami        lista degli esami sostenuti con il relativo range di voti
lode_exam               lista degli esami sostenuti con lode e senza lode
medie_matr_range        lista delle medie ponderate suddivise per range
"""

# ic_fc + lode_exam + medie_matr_range + range_voti_esami + lav_no_lav
insieme = lav_no_lav + ic_fc + range_voti_esami + medie_matr_range


def il_back():
    background = []
    dati = insieme
    for k in range(len(dati)):
        background.append(Clause.parse(str(dati[k])))
    return background


def gli_es():
    positivi = []
    negativi = []

    #TODO - capire la differenza tra "loc" e "iloc"
    elite = dataframe.loc[dataframe["VOTO_LAUREA"] == 110]
    # elite = dataframe.loc[dataframe["LODE_LAU"] == "L"]
    elite_mat = elite.iloc[:, 0].drop_duplicates()

    non_elite = dataframe.loc[(dataframe["VOTO_LAUREA"] != 110) & (~dataframe["VOTO_LAUREA"].isna())]
    non_elite_mat = non_elite.iloc[:, 0].drop_duplicates().to_list()
    non_elite_mat = list(map(str, non_elite_mat))

    for k in range(len(elite_mat)):
        positivi.append(Example({'X': "s" + str(elite_mat.iloc[k])}, Label.POSITIVE))
    for k in range(len(non_elite_mat)):
        negativi.append(Example({'X': "s" + str(non_elite_mat[k])}, Label.NEGATIVE))

    totale = positivi + negativi
    return totale