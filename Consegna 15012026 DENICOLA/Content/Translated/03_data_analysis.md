# Analisi Dati Incrociata (Cross-Tabular)

* **Ambito:** Ricerche di Marketing & Reportistica
* **Fonte Tecnica:** OpenAI Cookbook - Reliability Techniques

---

## 1. Obiettivo e Concetto
La **Cross-Tabular Analysis** consiste nel confrontare e incrociare fonti dati diverse (es. confrontare la Spesa Ads con le Vendite effettive sul CRM). L'obiettivo principale di questo modulo è azzerare il rischio di **"Allucinazione Numerica"**, ovvero la tendenza dell'IA a inventare correlazioni inesistenti o a sbagliare calcoli matematici complessi se non guidata correttamente.

## 2. Strategie per Prevenire l'Allucinazione
Per ottenere confronti affidabili ed evitare che l'IA "confabuli" risultati errati, è necessario forzare il modello a seguire un percorso logico rigido.

### 2.1 Scomposizione Sequenziale (Step-by-Step)
L'IA aumenta il rischio di errore se tenta di leggere due tabelle contemporaneamente. Bisogna imporre una progressione lineare.

> **PROMPT OPERATIVO**
>
> **Obiettivo:** Incrociare traffico del sito e fatturato.
>
> **Istruzioni:** > 1. Estrai dalla Tabella A (Traffico) solo le prime 5 pagine più visitate.
> 2. Cerca queste specifiche 5 pagine nella Tabella B (Vendite).
> 3. Solo dopo aver trovato i dati corrispondenti, crea la tabella di confronto.
> 4. Non calcolare medie totali finché la tabella non è completa.

### 2.2 Validazione delle Formule (Chain of Thought)
Mai chiedere "fai il calcolo". Bisogna chiedere all'IA di mostrare la formula matematica utilizzata prima di fornire il risultato. Questo permette al copywriter di verificare la logica del calcolo.

> **PROMPT OPERATIVO**
>
> **Task:** Calcola la variazione percentuale del budget tra mese A e mese B.
>
> **Vincolo Anti-Errore:** Prima di darmi il numero finale, scrivi esplicitamente la formula che stai usando (es. `((Nuovo - Vecchio) / Vecchio) * 100`). Se i dati sono incongruenti, scrivi "DATI NON COMPARABILI" invece di stimare.

### 2.3 Il "Monologo Interiore" per la Coerenza
Questa tecnica spinge l'IA a riflettere internamente sulla qualità dei dati prima di generare l'output finale.

> **ESEMPIO OPERATIVO**
>
> **Istruzione:** "Analizza i due report allegati. Prima di procedere, scrivi tra parentesi quadre una breve riflessione interna sulla coerenza dei nomi delle colonne (es. 'ID Cliente' è uguale a 'Email'?). Se trovi discrepanze, segnalale prima di incrociare i dati."


---

## 3. Scenari d'uso e Standardizzazione

### 3.1 Mappatura dei Campi (Context Grounding)
Spesso i file dei clienti hanno nomi diversi per le stesse informazioni. Bisogna "istruire" l'IA sulla legenda del file.

> **PROMPT OPERATIVO**
>
> **Ruolo:** Agisci come Data Analyst Senior.
> **Legenda:** > * La colonna 'Client_ID' del File A corrisponde a 'Email' nel File B.
> * La colonna 'Total_Spent' corrisponde al valore 'LTV'.
> **Task:** Unisci le righe usando queste chiavi.

---

## 4. Controllo Qualità (Checklist Anti-Allucinazione)
Prima di inserire i dati dell'IA in un report per il cliente, il team deve verificare questi 3 punti:

* [ ] **Verifica della Formula:** L'IA ha mostrato il calcolo logico? La formula è corretta?
* [ ] **Test del Campione:** Prendi una riga a caso e rifai il calcolo manualmente. Corrisponde?
* [ ] **Gestione dei Vuoti:** L'IA ha ignorato i dati mancanti o ha tentato di "inventarli" per riempire la tabella? (Assicurarsi che i campi vuoti siano rimasti tali).

## 5. Limitazioni Tecniche
* **Dataset estesi:** Questa procedura è sicura per file fino a 50 righe. Per file più grandi, l'IA potrebbe "dimenticare" i dati centrali. In quel caso, richiedere l'analisi tramite **Code Interpreter** (elaborazione via codice Python).