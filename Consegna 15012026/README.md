# Struttura del progetto

Questa cartella contiene i materiali, gli script e gli output relativi alla costruzione del manuale, dalla gestione dei file sorgente fino alla generazione dei formati finali.

## Struttura delle directory

```
├── Content/
├── Output/
├── Relazione/
├── build.py
├── cleaning.py
├── editorial_pipelineAPI.py
├── ePub.css
├── style.css
└── README.md
```
### Content
Contiene tutti i file di origine del manuale, inclusi:
- file grezzi di partenza
- file già modificati e processati tramite script

Questa directory rappresenta la base contenutistica del progetto.

### Output
Contiene i file di output finali, generati a partire dai contenuti presenti in Content tramite gli script di build e trasformazione.

Esempi tipici:
- file HTML
- file ePub
- file unificati del manuale

### Relazione
Comprende:
- la relazione del progetto
- le immagini e gli asset grafici associati alla relazione stessa

Questa directory è separata dai contenuti editoriali del manuale.

## Script

### build.py
Script di build del manuale.  
Permette di ottenere un unico file finale (o più formati) a partire dalle fonti presenti nella directory Content.

### cleaning.py
Script utilizzato per la pulizia dei file grezzi di partenza, con l’obiettivo di:
- rimuovere codice superfluo
- eliminare informazioni non necessarie
- normalizzare i contenuti prima delle fasi successive

### editorial_pipelineAPI.py
Script TO-BE (in evoluzione).  
È progettato per implementare una pipeline editoriale automatizzata che includa:
- pulizia dei contenuti
- traduzione
- utilizzo di intelligenza artificiale per l’elaborazione autonoma dei testi

## Fogli di stile

### style.css
Foglio di stile per la visualizzazione HTML del manuale.

### ePub.css
Foglio di stile dedicato alla formattazione ePub, ottimizzato per la lettura su dispositivi compatibili.

## Note
- Gli script sono pensati per essere utilizzati in sequenza logica: pulizia → elaborazione → build.
- La separazione tra Content, Output e Relazione garantisce chiarezza e modularità nel workflow.

