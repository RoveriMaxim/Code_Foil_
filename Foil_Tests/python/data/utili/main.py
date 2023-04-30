import pandas as pd
import openpyxl
import csv
from IPython import display
from arpeggio import ParserPython
from openpyxl import Workbook as wb
from arpeggio import visit_parse_tree

from methods import append_once, list_int64_toString
from grammar import comment


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataframe = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\F004-Carriere(150322).xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
# dataframe.dropna(inplace=True)
# dataframe[condizione per filtrare le righe eliminando le vuote]
data_media = dataframe[~dataframe["MEDIA P"].isna()]
data_voto = dataframe[~dataframe["voto esame"].isna()]



""" print("Matricole convertite: ", dataframe['MATRICOLA'].dtypes)
 """
# print("\n", "DTypes:: ", "\n", dataframe.dtypes, "\n")


indice = data_media.iloc[:, 0]
matricole = []
matr_once = []
for k in range(len(indice)):
    matricole.append(indice.iloc[k])
for i in range(len(matricole)):
    matricole[i] = str(matricole[i])

matricole = list(map(str, matricole))
matr_once = append_once(matricole)
matr_once = list(map(str, matr_once))
""" print("____________________________________________________________________", "\n",
      "STUDENTS_MATR_ONCE::: ", "\n", students_matr, "\n") """


# Z
indice_ = data_media.iloc[:, 25]
AD_DES = []
a_d = []
for k in range(len(indice_)):
    AD_DES.append(indice_.iloc[k])
a_d = append_once(AD_DES)
""" print("____________________________________________________________________", "\n",
      "AD_DES_ONCE::: ", "\n", a_d, "\n") """


voti_ = [0 if str(x) == 'nan' else x for x in data_media['voto esame']]
medie_matr = []
for k in range(len(voti_)):
    if 18 <= voti_[k] <= 22:
        medie_matr.append(matricole[k] + " v_18_22 " + AD_DES[k])
    elif 23 <= voti_[k] <= 27:
        medie_matr.append(matricole[k] + " v_23_27 "  + AD_DES[k])
    elif 28 <= voti_[k] <= 30:
        medie_matr.append(matricole[k] + " v_28_30 "  + AD_DES[k])
    else:
        medie_matr.append(matricole[k] + " non superato "  + AD_DES[k])
""" for p in range(len(medie_matr)):
    print(medie_matr[p]) """


esa = data_media.iloc[:, 25]
esami = []
for k in range(len(esa)):
    if "ALGORITMI E STRUTTURE DATI" in esa.iloc[k]:
        esami.append(matricole[k] + " algoritmi")
    elif "FONDAMENTI DI SICUREZZA" in esa.iloc[k]:
        esami.append(matricole[k] + " fondamenti")
    elif "ALGEBRA E GEOMETRIA" in esa.iloc[k]:
        esami.append(matricole[k] + " geometria")
""" for p in range(len(esami)):
    print(esami[p]) """












""" ind = data_media.iloc[:, 6]
STATO_OCCUP_COD = []
stat_occup = []
for k in range(len(ind)):
    STATO_OCCUP_COD.append(ind.iloc[k])
stat_occup = append_once(STATO_OCCUP_COD)
print("____________________________________________________________________", "\n",
      "STATO_OCCUP_ONCE::: ", "\n", stat_occup, "\n")


indice1 = data_media.iloc[:, 8]
CDS_COD = []
CD = []
for k in range(len(indice1)):
    CDS_COD.append(indice1.iloc[k])
CD = append_once(CDS_COD)
print("____________________________________________________________________", "\n",
      "CDS_COD_ONCE::: ", "\n", CD, "\n")


indice2 = data_media.iloc[:, 9]
SEDE_ID = []
sede = []
for k in range(len(indice2)):
    SEDE_ID.append(indice2.iloc[k])
sede = append_once(SEDE_ID)
print("____________________________________________________________________", "\n",
      "SEDE_ID_ONCE::: ", "\n", sede, "\n")

# S
indice3 = data_media.iloc[:, 18]
ANNO_CORSO_ULTIMA_ISCR = []
a_u_i = []
for k in range(len(indice3)):
    ANNO_CORSO_ULTIMA_ISCR.append(indice3.iloc[k])
a_u_i = append_once(ANNO_CORSO_ULTIMA_ISCR)
print("____________________________________________________________________", "\n",
      "ANNO_CORSO_ULTIMA_ISCR_ONCE::: ", "\n", a_u_i, "\n")

# T
indice4 = data_media.iloc[:, 19]
TIPO_ISCR_ULTIMA_ISCR = []
t_i_u_i = []
for k in range(len(indice4)):
    TIPO_ISCR_ULTIMA_ISCR.append(indice4.iloc[k])
t_i_u_i = append_once(TIPO_ISCR_ULTIMA_ISCR)
print("____________________________________________________________________", "\n",
      "TIPO_ISCR_ULTIMA_ISCR_ONCE::: ", "\n", t_i_u_i, "\n")

# U
indice5 = data_media.iloc[:, 20]
DATA_TITOLO = []
d_t = []
for k in range(len(indice5)):
    DATA_TITOLO.append(indice5.iloc[k])
d_t = append_once(DATA_TITOLO)
print("____________________________________________________________________", "\n",
      "DATA_TITOLO_ONCE::: ", "\n", d_t, "\n")

# V
indice6 = data_media.iloc[:, 21]
VOTO_LAUREA = []
v_l = []
for k in range(len(indice6)):
    VOTO_LAUREA.append(indice6.iloc[k])
v_l = append_once(VOTO_LAUREA)
print("____________________________________________________________________", "\n",
      "VOTO_LAUREA_ONCE::: ", "\n", v_l, "\n")


# W
indice7 = data_media.iloc[:, 22]
LODE_LAU = []
l_l = []
for k in range(len(indice7)):
    LODE_LAU.append(indice7.iloc[k])
l_l = append_once(LODE_LAU)
print("____________________________________________________________________", "\n",
      "LODE_LAU_ONCE::: ", "\n", l_l, "\n")


# X
indice8 = data_media.iloc[:, 23]
ANNO_AD = []
a_a = []
for k in range(len(indice8)):
    ANNO_AD.append(indice8.iloc[k])
a_a = append_once(ANNO_AD)
print("____________________________________________________________________", "\n",
      "ANNO_AD_ONCE::: ", "\n", a_a, "\n") """


# Y
indice9 = data_media.iloc[:, 24]
AD_COD = []
a_c = []
for k in range(len(indice9)):
    AD_COD.append(indice9.iloc[k])
a_c = append_once(AD_COD)
""" print("____________________________________________________________________", "\n",
      "AD_COD_ONCE::: ", "\n", a_c, "\n") """


# Z
""" indice_ = data_media.iloc[:, 25]
AD_DES = []
a_d = []
for k in range(len(indice_)):
    AD_DES.append(indice_.iloc[k])
a_d = append_once(AD_DES)
print("____________________________________________________________________", "\n",
      "AD_DES_ONCE::: ", "\n", a_d, "\n")


# aa
indice_0 = data_media.iloc[:, 26]
STA_SCE_COD = []
s_s_c = []
for k in range(len(indice_0)):
    STA_SCE_COD.append(indice_0.iloc[k])
s_s_c = append_once(STA_SCE_COD)
print("____________________________________________________________________", "\n",
      "STA_SCE_COD_ONCE::: ", "\n", s_s_c, "\n")


# ab
indice_1 = data_media.iloc[:, 27]
AA_FREQ_ID = []
a_f_i = []
for k in range(len(indice_1)):
    AA_FREQ_ID.append(indice_1.iloc[k])
a_f_i = append_once(AA_FREQ_ID)

a_f_i.sort()
print("____________________________________________________________________", "\n",
      "AA_FREQ_ID_ONCE::: ", "\n", a_f_i, "\n")

# ae
indice_1 = data_media.iloc[:, 30]
voto_esame = []
v_e = []
for k in range(len(indice_1)):
    voto_esame.append(indice_1.iloc[k])
v_e = append_once(voto_esame)
print("____________________________________________________________________", "\n",
      "VOTO_ESAME_ONCE::: ", "\n", v_e, "\n")


# ag
indice_2 = data_media.iloc[:, 32]
tipo_ric = []
t_r = []
for k in range(len(indice_2)):
    tipo_ric.append(indice_2.iloc[k])
t_r = append_once(tipo_ric)
print("____________________________________________________________________", "\n",
      "TIPO_RIC_ONCE::: ", "\n", t_r, "\n")


# ai
indice_3 = data_media.iloc[:, 34]
MEDIA_P = []
m_p = []
for k in range(len(indice_3)):
    MEDIA_P.append(indice_3.iloc[k])
m_p = append_once(MEDIA_P)
print("____________________________________________________________________", "\n",
      "MEDIA_P_ONCE::: ", "\n", m_p, "\n") """


########################################################################
########################################################################
""" print(len(matr_once))
print(len(AD_COD)) """

""" esami_x_studente = []
new_array = []

for k in range(len(matr_once)):
    for i in range(len(matricole)):
        while matricole[i] == matr_once[k]:
            esami_x_studente.append(matr_once[k] + " " + AD_COD[i])
            break


print("____________________________________________________________________", "\n",
        "ESAMI_X_STUDENTE::: ", "\n", esami_x_studente, "\n")
 """











""" print("\n", "________________________________________________________________________", " File Columns ", 
            "________________________________________________________________________")
print(file.columns) """


""" print("\n", "________________________________________________________________________", " File iloc _0:5, 0:2_", 
"________________________________________________________________________", "\n")
print(file.iloc[0:5, 0:2])
print("")

print("\n", "________________________________________________________________________", " Data File isna", 
"________________________________________________________________________", "\n")

data_file = file.isna() """