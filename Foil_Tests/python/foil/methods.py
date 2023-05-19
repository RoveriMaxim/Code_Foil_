import csv
from openpyxl import Workbook
from inflect import engine
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3


# Read csv file and convert it to xlsx
def csv_to_xlsx(csv_file_input, xlsx_name_output):
    wb = Workbook()
    wba = wb.active
    with open(csv_file_input, 'r') as f:
        for row in csv.reader(f):
            wba.append(row)
            nuovo_file = wb.save(xlsx_name_output)
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

def num_ord_fem(numero):
    numeri = {
        1: "prima",
        2: "seconda",
        3: "terza",
        4: "quarta",
        5: "quinta",
    }

    if numero in numeri:
        return numeri[numero]
    else:
        return str(numero)  # Restituisce il numero come stringa se non ha una corrispondenza

def prep_lav(matr_no_dupl):
    lav_no_lav = []
    for _, distinct_row in matr_no_dupl.iterrows():
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
    return lav_no_lav

def prep_ic_fc(matr_no_dupl):
    ic_fc = []
    for _, matr in matr_no_dupl.iterrows():
        if "IC" in str(matr[19]):
            ic_fc.append("in_corso" + "(s" + matr[0] + ").")
        else:
            ic_fc.append("fuori_corso" + "(s" + matr[0] + ").")
    return ic_fc

def prep_medie(matr_no_dupl):
    range_medie_matr = []
    for _, medie in matr_no_dupl.iterrows():
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
    return range_medie_matr

def prep_voti(data):
    range_voti_esami = []
    for _, row in data.iterrows():
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
    return range_voti_esami
    
def colonna_scelta(colonna, matr_no_dupl, data, insieme):
    print("\ncolonna: ", colonna)
    if colonna == "Descrizione <studente lavoratore o non>":
        stampa_occupazione()
        insieme = insieme + prep_lav(matr_no_dupl)

    elif colonna == "Status iscrizione <in corso o non>":
        stampa_in_corso()
        insieme = insieme + prep_ic_fc(matr_no_dupl)

    elif colonna == "Valutazione esami":
        stampa_voti()
        insieme = insieme + prep_voti(data)

    elif colonna == "Media ponderata":
        stampa_media()
        insieme = insieme + prep_medie(matr_no_dupl)

    return insieme

def stampa_occupazione():
    print("\tnon_occup_(s[MAT]). = studente non occupato e relativa matricola MAT")
    print("\toccup_(s[MAT]). = studente occupato e relativa matricola MAT")
    print("\tstud_lav_(s[MAT]). = studente lavoratore con tempo di studio < 50% e relativa matricola MAT")
    print("\tnon_lav_gr75_(s[MAT]). = studente non lavoratore con tempo di studio > 75% e relativa matricola MAT")
    print("\tnan_fulltime_(s[MAT]). = studente con stato di occupazione non fornito e relativa matricola MAT")

def stampa_in_corso():
    print("\tin_corso(s[MAT]). = studente in corso con relativa matricola MAT")
    print("\tfuori_corso(s[MAT]). = studente fuori corso con relativa matricola MAT")

def stampa_voti():
    print("\tp_18_25(s[MAT]). = votazione di programmazione tra 18 e 25 e relativa matricola MAT")
    print("\tp_26_30(s[MAT]). = votazione di programmazione tra 26 e 30 e relativa matricola MAT")
    print("\ta_18_25(s[MAT]). = votazione di algoritmi e strutture dati tra 18 e 25 e relativa matricola MAT")
    print("\ta_26_30(s[MAT]). = votazione di algoritmi e strutture dati tra 26 e 30 e relativa matricola MAT")
    print("\tb_18_25(s[MAT]). = votazione di basi di dati tra 18 e 25 e relativa matricola MAT")
    print("\tb_26_30(s[MAT]). = votazione di basi di dati tra 26 e 30 e relativa matricola MAT")
    print("\tr_18_25(s[MAT]). = votazione di reti ti telecomunicazioni tra 18 e 25 e relativa matricola MAT")
    print("\tr_26_30(s[MAT]). = votazione di reti ti telecomunicazioni tra 26 e 30 e relativa matricola MAT")
    print("\ti_18_25(s[MAT]). = votazione di inglese tra 18 e 25 e relativa matricola MAT")
    print("\ti_26_30(s[MAT]). = votazione di inglese tra 26 e 30 e relativa matricola MAT")
    print("\tl_18_25(s[MAT]). = votazione di logica tra 18 e 25 e relativa matricola MAT")
    print("\tl_26_30(s[MAT]). = votazione di logica tra 26 e 30 e relativa matricola MAT")
    print("\tf_18_25(s[MAT]). = votazione di fondamenti di sicurezza tra 18 e 25 e relativa matricola MAT")
    print("\tf_26_30(s[MAT]). = votazione di fondamenti di sicurezza tra 26 e 30 e relativa matricola MAT")
    print("\tlib_18_25(s[MAT]). = votazione di laboratorio interdisciplinare B tra 18 e 25 e relativa matricola MAT")
    print("\tlib_26_30(s[MAT]). = votazione di laboratorio interdisciplinare B tra 26 e 30 e relativa matricola MAT")

def stampa_media():
    print("\tm_18_20_(s[MAT]). = studente con media ponderata tra 18 e 20 e relativa matricola MAT")
    print("\tm_21_24_(s[MAT]). = studente con media ponderata tra 21 e 24 e relativa matricola MAT")
    print("\tm_25_27_(s[MAT]). = studente con media ponderata tra 25 e 27 e relativa matricola MAT")
    print("\tm_28_30_(s[MAT]). = studente con media ponderata tra 28 e 30 e relativa matricola MAT")
    print("\tesami_sostenuti_insufficienti(s[MAT]). = studente con nessun esame sostenuto e relativa matricola MAT")
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