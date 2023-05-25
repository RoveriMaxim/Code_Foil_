import pandas as pd
from models import Clause, Example, Label
from methods import num_ord_fem, prep_ic_fc, prep_lav, prep_medie, prep_voti, colonna_scelta, stampa_in_corso, stampa_occupazione, stampa_media, stampa_voti


# imposto il numero massimo di righe e colonne visualizzate su None, che significa "nessun limite"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# leggo il file excel
# converto la colonna MATRICOLA in stringa
# datamedia contiene tutte le righe (eccetto quelle null) di tutte le colonne
dataframe = pd.read_excel('DS_Uninsubria.xlsx')
dataframe['MATRICOLA'] = dataframe['MATRICOLA'].astype(str)
data = dataframe[~dataframe["MEDIA P"].isna()]

 #frequentato, programmato, superato 
colonne_disponibili = data.columns.tolist()
# Verifica se i nomi delle colonne inseriti sono validi
""" colonne_non_trovate = [col for col in check_col if col not in check_col]
if colonne_non_trovate:
    print("I seguenti nomi di colonne non sono presenti nel dataset:")
    for col in colonne_non_trovate:
        print(col)
else:
for colonna in ids:
        if colonna == "1":
            colonne_selezionate.append("MATRICOLA")
        elif colonna == "2":
            colonne_selezionate.append("Descrizione <studente lavoratore o non>")
        elif colonna == "3":
            colonne_selezionate.append("Status iscrizione <in corso o non>")
        elif colonna == "4":
            colonne_selezionate.append("Valutazione esami")
        elif colonna == "5":
            colonne_selezionate.append("Media ponderata")
        elif colonna == "6":
            colonne_selezionate.append("Status esame <Frequentato, Superato, Programmato>")
        elif colonna == "7":
            colonne_selezionate.append("Data di nascita")
        else:
            print("ID non valido")
            break """
""" check_col = ["1", "2", "3", "4", "5", "6", "7"] 
id_colonne = []
ids = []
colonne_selezionate = []

print("Inserisci l'ID delle colonne che vuoi selezionare tra quelle presenti nel seguente elenco: " + "\n")
print("ID: 1    MATRICOLA" + "\n" + "ID: 2    Descrizione <studente lavoratore o non>" + "\n" + "ID: 3    Status iscrizione <in corso o non>" + "\n" + "ID: 4    Valutazione esami" + "\n" + "ID: 5    Media ponderata" + "\n" + "ID: 6    Status esame <Frequentato, Superato, Programmato>" + "\n" + "ID: 7    Data di nascita")
print("")
for i in range(4):
    id_colonne = input(f"Inserisci l'ID della colonna {i+1}: ")
    ids.append(id_colonne)

# Verifica se i nomi delle colonne inseriti sono validi
colonne_non_trovate = [col for col in check_col if col not in check_col]
if colonne_non_trovate:
    print("I seguenti nomi di colonne non sono presenti nel dataset:")
    for col in colonne_non_trovate:
        print(col)
else:
    mapping_colonne = {
        "1": "MATRICOLA",
        "2": "Descrizione <studente lavoratore o non>",
        "3": "Status iscrizione <in corso o non>",
        "4": "Valutazione esami",
        "5": "Media ponderata",
        "6": "Status esame <Frequentato, Superato, Programmato>",
        "7": "Data di nascita",
    }
    for colonna in ids:
        if colonna in mapping_colonne:
            colonne_selezionate.append(mapping_colonne[colonna])
        else:
            print("ID non valido")
            break

print("")
print("colonne selezionate: " + "\n")
for colonna in colonne_selezionate:
    print(colonna)
print("") """

def prepare_data():
    ids = []
    colonne_selezionate = []

    check_col = ["1", "2", "3", "4"]
    mapping_colonne = {
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

    colonne_selezionate = [mapping_colonne.get(col) for col in ids if col in mapping_colonne]

    colonne_non_trovate = [col for col in ids if col not in check_col]
    insieme = []
    matr_no_dupl = dataframe.drop_duplicates(subset=['MATRICOLA'])

    if all(id_col == "" for id_col in ids):
        print("________________________________________________________________________")
        print("\nNon hai inserito nessun ID. Procedo con i dati default...")
        print("\nDati di default:")
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

    # ____________________________________________________________________________________________________________________________
    # Creo due liste matricole, una con le matricole e una con le matricole e il predicato s
    # Converto le matricole in stringhe (object)
    # Creo poi una lista con le matricole senza duplicati

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
