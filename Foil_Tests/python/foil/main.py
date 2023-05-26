import pandas as pd
from models import Clause, Example, Label
from methods import *

# imposto il numero massimo di righe e colonne
# visualizzate su None, che significa "nessun limite"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# leggo il file excel
# converto la colonna MATRICOLA in stringa
# data contiene tutte le righe (eccetto quelle null) di tutte le colonne
dataframe = pd.read_excel('DS_Uninsubria_.xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
data = dataframe[~dataframe["MATRICOLA"].isna()]


def prepare_data():
    ids = []
    colonne_selezionate = []

    check_col = ["1", "2", "3", "4"]
    diz_colonne = {
        "1": "Descrizione <studente lavoratore o non>",
        "2": "Status iscrizione <in corso o non>",
        "3": "Valutazione esami",
        "4": "Media ponderata",
    }

    print(
        "\nPer iniziare la valutazione dei letterali inserisci l'ID delle colonne che vuoi selezionare tra quelle presenti nel seguente elenco:\n"
        "\n"
        "ID: 1    Descrizione <studente lavoratore o non>\n"
        "ID: 2    Status iscrizione <in corso o non>\n"
        "ID: 3    Valutazione esami\n"
        "ID: 4    Media ponderata\n"
    )

    for i in range(4):
        posizione = num_ord_fem(i + 1)
        id_colonna = input(f"Inserisci l'ID per valutare la {posizione} colonna: ")
        ids.append(id_colonna)

    colonne_selezionate = [diz_colonne.get(col) for col in ids if col in diz_colonne]
    colonne_non_trovate = [col for col in ids if col not in check_col]
    
    insieme = []
    matr_no_dupl = dataframe.drop_duplicates(subset=['MATRICOLA'])

    if all(id_col == "" for id_col in ids):

        # Lista studente lavoratore o non lavoratore
        lav_no_lav = prep_lav(matr_no_dupl)
        # Lista studenti fuori corso o non fuori corso
        ic_fc = prep_ic_fc(matr_no_dupl)
        # Lista delle medie ponderate suddivise per range
        range_medie_matr = prep_medie(matr_no_dupl)
        # Lista degli esami suddivisi per range di voto
        range_voti_esami = prep_voti(data)

        print("\nColonna Stato Occupazionale:")
        stampa_occupazione()
        print("\nColonna Stato Iscrizione:")
        stampa_in_corso()
        print("\nColonna Media Ponderata:")
        stampa_media()
        print("\nColonna Range Voti Esami:")
        stampa_voti()
        print("________________________________________________________________________")
        print("\n\n")
        """
        lav_no_lav              lista degli studenti lavoratori e non
        ic_fc                   lista degli studenti in corso e fuori corso (?)
        range_voti_esami        lista degli esami sostenuti con il relativo range di voti
        range_medie_matr        lista delle medie ponderate suddivise per range 
        """
        insieme = range_voti_esami + lav_no_lav + ic_fc + range_medie_matr

    elif not colonne_non_trovate:
        print("________________________________________________")
        print("I dati delle colonne selezionate hanno la seguente struttura:\n")
        for colonna in colonne_selezionate:
           insieme = colonna_scelta(colonna, matr_no_dupl, data, insieme)

        print("\nProcedo con la valutazione...\n")
    else:
        for i in range(len(ids)):
            if ids[i] == "":
                ids[i] = "x"
        print("________________________________________________")
        print("\nI seguenti ID di colonne non sono validi:")
        for col in ids:
            if col == "x" or col not in check_col:
                print(col)
        print("________________________________________________")
        print("I dati delle colonne selezionate hanno la seguente struttura:\n")
        for colonna in colonne_selezionate:
            insieme = colonna_scelta(colonna, matr_no_dupl, data, insieme)
        print("\nProcedo con la valutazione...\n")
    return insieme


def il_back(insieme):
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


        
""" # PROVA
gruppi = dataframe.groupby('MATRICOLA')
# crea una lista degli esami per ogni matricola
lista_esami = gruppi['AD_COD'].unique()
# conta il numero di esami superati per ogni matricola
conteggio_esami = dataframe['MATRICOLA'].value_counts()
# FINE PROVA """
