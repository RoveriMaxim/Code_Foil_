import numpy as np
import pandas as pd
import openpyxl
import csv
from IPython import display
from arpeggio import ParserPython
from openpyxl import Workbook as wb
from arpeggio import visit_parse_tree

from models import Clause, Example, Label


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
dataframe = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\Carr.xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
# datamedia contiene tutte le righe (eccetto quelle null) di tutte le colonne 
data_media = dataframe[~dataframe["MEDIA P"].isna()]


indice = data_media.iloc[:, 0]
matricole = []
for k in range(len(indice)):
    matricole.append(indice.iloc[k]) # Creo una lista di matricole (int64)
for i in range(len(matricole)):
    matricole[i] = str(matricole[i]) # Converto le matricole in stringhe (object) 

dropped_matr = dataframe.drop_duplicates(subset=['MATRICOLA'])  # non considero le matricole
                                                                # ripetute

matricole = list(map(str, matricole))
for k in range(len(matricole)):
    matricole[k] = "(s" + matricole[k] + ")." # Aggiungo il predicato s alle matricole


ad_des = data_media.iloc[:, 25]
lista_nomi_esami = []
for k in range(len(ad_des)):
    lista_nomi_esami.append(ad_des.iloc[k] + matricole[k])  # Creo una lista di _esami _sostenuti dagli
                                                        # _alunni + matricole(object)

""" 
indice = data_media.iloc[:, 19]
i_f_corso = []
for k in range(len(indice)):
    if "IC" in str(indice.iloc[k]):
        i_f_corso.append("in_corso" + matricole[k])
    else:
        i_f_corso.append("fuori_corso" + matricole[k])   # Creo una lista di alunni _in corso
                                                        # e _fuori corso  + _matricole(object)
 """

indice = data_media.iloc[:, 7]
worker = []
for k in range(len(indice)):
    if "non lavoratore: tempo studio > 75%" or "Non occupato-Iscrito full time" in str(indice.iloc[k]):
        worker.append("nonLavoratore" + matricole[k])# lista studenti non lavoratori
    elif "lavoratore: tempo studio < 75%" in str(indice.iloc[k]):
        worker.append("lavoratore" + matricole[k])# lista studenti lavoratori


v_lau = []
for index, matr in dropped_matr.iterrows():
    if str(matr[21]) != "nan" or matr[21] > 99:
        if (matr[21] == 110 and matr[22] == "L"):
            v_lau.append("lau_lode" + "(s" + matr[0] + ").")
        elif 100 <= matr[21] <= 110:
            v_lau.append("l" + "(s" + matr[0] + ").")


#VOTI ESAME
l_voti = data_media.iloc[:, 30] # salvo in range_voti[] i voti di laurea dei vari stuenti
                                # con le relative matricole
range_voti_esami = []
l_voti = [0 if str(x) == "nan" else x for x in l_voti]
for k in range(len(l_voti)):
    if (18 <= l_voti[k] <= 25  and  lista_nomi_esami[k] == "ALGORITMI E STRUTTURE DATI" + matricole[k]):
        range_voti_esami.append("a_18_25" + matricole[k])
    elif (26 <= l_voti[k] <= 30  and  lista_nomi_esami[k] == "ALGORITMI E STRUTTURE DATI" + matricole[k]):
        range_voti_esami.append("a_26_30" + matricole[k])

    elif (18 <= l_voti[k] <= 25  and  lista_nomi_esami[k] == "FONDAMENTI DI SICUREZZA" + matricole[k]):
        range_voti_esami.append("f_18_25" +  matricole[k])
    elif (26 <= l_voti[k] <= 30  and  lista_nomi_esami[k] == "FONDAMENTI DI SICUREZZA" + matricole[k]):
        range_voti_esami.append("f_26_30" + matricole[k])

    elif (18 <= l_voti[k] <= 25  and  lista_nomi_esami[k] == "ALGEBRA E GEOMETRIA" + matricole[k]):
        range_voti_esami.append("g_18_25" + matricole[k])
    elif (26 <= l_voti[k] <= 30  and  lista_nomi_esami[k] == "ALGEBRA E GEOMETRIA" + matricole[k]):
        range_voti_esami.append("g_26_30" + matricole[k])
    else:
        range_voti_esami.append("est" + matricole[k])
    

media_p = []
for index, matr in dropped_matr.iterrows():
    media_p.append(str(matr[34]) + "(s" + matr[0] + ").")

in_c_or_out_c = []
for index, matr in dropped_matr.iterrows():
    if "IC" in str(matr[19]):
        in_c_or_out_c.append("in_corso" + "(s" + matr[0] + ").")
    else:
        in_c_or_out_c.append("fuori_corso" + "(s" + matr[0] + ").")


# Lode:  833
# Non lode:  32629
indice = data_media.iloc[:, 22]
lode_esame = []
for k in range(len(indice)):
    if "L" in str(indice.iloc[k]):
        lode_esame.append("lode" + matricole[k])
    else:
        lode_esame.append("non_lode" + matricole[k])


l_voti = list(map(int, l_voti))
l_voti = ["dipEst" if x == 0 else x for x in l_voti]
l_voti = list(map(str, l_voti))


voti_esami_matr = []
for k in range(len(l_voti)):
    voti_esami_matr.append(l_voti[k] + matricole[k])


for k in range(len(in_c_or_out_c)):
    in_c_or_out_c[k] = in_c_or_out_c[k] + matricole[k]


# range_voti_esami  lista degli esami sostenuti con il relativo range di voti
# media_p           lista delle medie pesate per singolo studente
# voti_esami_matr   lista dei voti degli esami sostenuti
# lista_nomi_esami  lista degli esami
# worker            lista degli studenti lavoratori e non
# v_lau             lista dei voti di laurea
# i_f_corso         lista degli studenti in corso e fuori corso
insieme = range_voti_esami + worker + in_c_or_out_c


def il_back():
    background = []
    dati = insieme

    for k in range(len(dati)):
        background.append(Clause.parse(str(dati[k])))

    return background


def gli_es():
    positivi = []
    negativi = []
    elite = dataframe.loc[dataframe["VOTO_LAUREA"] == 110]
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
