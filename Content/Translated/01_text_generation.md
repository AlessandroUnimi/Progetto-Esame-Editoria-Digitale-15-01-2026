# Creazione Contenuti (Text Generation)

* **Ambito:** Copywriting & Social Media
* **Fonte Tecnica:** OpenAI Cookbook - Prompt Engineering

---

## 1. Obiettivo e Concetto
Questa sezione supporta il team nell'uso quotidiano degli strumenti generativi per la scrittura. L'obiettivo non è sostituire il copywriter, ma fornire semilavorati di alta qualità.

## 2. Strategie di Prompt Design

### 2.1 Chiarezza e Dettaglio (Context Setting)
I modelli non leggono nel pensiero. Fornire contesto è vitale. Di seguito tre confronti operativi tra prompt inefficaci ed efficaci.

> **SCENARIO A: Social Media**
>
> ❌ **Generico (Sconsigliato):**
> "Scrivi un post sui saldi."
>
> ✅ **Dettagliato (Consigliato):**
> "Scrivi un post Facebook per i saldi invernali del cliente 'ModaX'. Target: donne 25-40 anni. Tono: urgente ed entusiasta. Includi il codice 'SALDI50'."

> **SCENARIO B: Tone of Voice**
>
> ❌ **Generico (Sconsigliato):**
> "Scrivi una mail."
>
> ✅ **Dettagliato (Consigliato):**
> "Agisci come un **Account Manager Senior**. Scrivi una mail formale ma empatica per gestire un reclamo cliente."

> **SCENARIO C: Project Management**
>
> ❌ **Generico (Sconsigliato):**
> "Riassumi il meeting."
>
> ✅ **Dettagliato (Consigliato):**
> "Riassumi le note del meeting in un paragrafo. Poi elenca i 'Next Steps' assegnati a ogni membro del team in una lista puntata."

### 2.2 Definizione del Ruolo (Persona Adoption)

> **ESEMPIO OPERATIVO**
>
> **Ruolo:** Agisci come un **Senior Copywriter** esperto in Neuromarketing. Usa principi di persuasione in ogni testo che generi.
>
> **Task:** Scrivi una landing page per il nostro nuovo corso di "Digital Strategy".

### 2.3 Delimitatori e Input Separati

> **ESEMPIO OPERATIVO**
>
> **User:** Riassumi il testo delimitato da triple virgolette in un titolo (H1).
>
> **Input:**
> """
> [Inserire qui il testo lungo del brief del cliente]
> """

### 2.4 Esempi Pratici (Few-Shot Prompting)

> **ESEMPIO OPERATIVO**
>
> **Sistema:** Rispondi con uno stile coerente (Tone of Voice: Lussuoso e Minimalista).
>
> **User:** Descrivi la pazienza.
> **AI:** Il fiume che scava la valle più profonda scorre da una sorgente modesta.
>
> **User:** Descrivi il nostro nuovo servizio di consulenza Premium.

---

## 3. Strategie Avanzate e Ragionamento

### 3.1 Classificazione degli Intenti

> **ESEMPIO OPERATIVO**
>
> **Istruzione:** Classifica i commenti social in arrivo.
>
> **Logica:**
> * Assistenza -> Chiedi numero ordine.
> * Lead -> Invia brochure.
> * Spam -> Ignora.
>
> **Input:** "Quanto costa il modello rosso?"
> **Output:** Lead.

### 3.2 Ragionamento (Chain of Thought)

> **ESEMPIO OPERATIVO**
>
> **Istruzione:** Prima analizza il testo fornito. Identifica punti di forza e debolezze rispetto alle regole SEO.
>
> **Vincolo:** **Solo dopo aver fatto l'analisi**, scrivi la versione rivista dell'articolo.
>
> **Input:** [Bozza Articolo del Junior Copywriter]

### 3.3 Monologo Interiore

> **ESEMPIO OPERATIVO**
>
> **Step 1 (Ragionamento Nascosto):** Ragiona su quale sia la migliore risposta diplomatica al reclamo del cliente. Metti questo ragionamento tra tripli backticks.
>
> **Step 2 (Output Finale):** Scrivi la risposta finale pulita da inviare.
>
> **Input:** "Voglio il rimborso immediato!"

---

## 4. Strumenti Esterni e Workflow

### 4.1 Grounding (Uso di Riferimenti)

> **ESEMPIO OPERATIVO**
>
> **Istruzione:** Usa le **Brand Guidelines** fornite tra triple virgolette per scrivere il copy. Se il tono richiesto non è chiaro, scrivi "Informazione mancante".
>
> **Testo Riferimento:** """[Incollare qui le Linee Guida]"""
>
> **Task:** Scrivi una email di benvenuto.

### 4.2 Code Interpreter

> **ESEMPIO OPERATIVO**
>
> **Istruzione:** Scrivi ed esegui codice Python.
>
> **Task:** Ho allegato il CSV con i dati della campagna Google Ads. Calcola il CPC medio e il ROI per ogni gruppo di annunci. Non calcolarlo a mente, usa il codice.

---

## 5. Controllo Qualità (Checklist)

> **VERIFICA AUTOMATIZZATA**
>
> **Istruzione:** Ti fornirò una Bio aziendale generata. Verifica se rispetta questi criteri.
>
> **Criteri:**
> 1. Menziona l'anno di fondazione (2010).
> 2. Usa la parola chiave "Innovazione".
> 3. Non supera i 160 caratteri.
>
> **Output:** Per ogni punto scrivi "SÌ" o "NO".