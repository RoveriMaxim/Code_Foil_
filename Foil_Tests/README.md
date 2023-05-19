# CodeFoil

**Progetto Roveri Maxim - Induzione di Regole con Algoritmo Foil.**

![Stato del progetto](https://img.shields.io/badge/Stato-Sviluppo%20Attivo-brightgreen)

## Stato del Progetto
Il progetto è attualmente in fase di sviluppo attivo e riceve regolarmente aggiornamenti e miglioramenti.

# Descrizione
Questo progetto è volto alla generazione di regole ed ipotesi a partire da un set di dati, più o meno grande. L'algoritmo utilizzato per questo scopo è il FOIL, che, essendo un algoritmo di Inductive Logic Programming (ILP) consente di indurre regole logiche a partire da esempi specifici.

# Installazione di librerie
Il programma necessita l'installazione di alcune librerie, quelle necessarie sono: -csv e -json (se le estensioni dei file sono .csv o .json, diverse da .xlsx), -arpeggio, -math, -collections, -itertools, -typing, -openpyxl, -enum, -pyparsing, -re.

# Il progetto è strutturato in 3 macro parti:
## 1_ main:
contiene il dataset ed elabora i dati in base al fine dell'utente che li sceglie, in modo che abbiano un senso rispettivamente al target scelto.
## 2_ file che esegue il foil:
chiamato "run". Qui il programma genera i dati che verranno poi passati all'algoritmo facendone il parsing. E' il file da eseguire per poter usufruire del programma.
## 3_ gli altri file:
in questi, i dati del file di lavoro vengono elaborati.

# Al momento i file non sono suddivisi in packages.

## Licenza
Questo progetto è sotto la licenza di Roveri Maxim. Consulta il file LICENZA per ulteriori informazi.
