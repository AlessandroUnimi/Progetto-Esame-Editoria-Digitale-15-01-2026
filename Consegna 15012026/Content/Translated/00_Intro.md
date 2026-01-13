---
title: "Manuale Operativo IA"
subtitle: "Agenzia di Comunicazione Digitale - Versione 1.0"
author: "Alessandro De Nicola"
date: "Gennaio 2026"
geometry: "left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm"
header-includes:
 - \usepackage{tcolorbox}
 - \definecolor{boxgray}{RGB}{240,247,251}
 - \definecolor{boxline}{RGB}{0,80,158}
 - \renewenvironment{quote}{\begin{tcolorbox}[colback=boxgray,colframe=boxline,left=5pt,right=5pt,boxrule=1pt,arc=0pt]}{\end{tcolorbox}}
 - \usepackage{titlesec}
 - \titleformat{\section}{\huge\bfseries\color{boxline}}{}{0em}{}
 - \titlespacing{\section}{0pt}{1cm}{0.5cm}
 - |
   \renewcommand{\maketitle}{
     \begin{titlepage}
       \centering
       \vspace*{3cm}
       
       % 1. TITOLO (Solo questo è BLU)
       {\Huge\bfseries\color{boxline} Manuale Operativo IA \par}
       
       \vspace{1.5cm}
       
       % 2. SOTTOTITOLO / CLIENTE 
       {\Large\color{black} \textbf Agenzia di Comunicazione Digitale \par}
       {\large\color{gray} Versione 1.0 \par}
       
       \vspace{3cm}
       
       % 3. AUTORE (Nero)
       {\large\bfseries Alessandro De Nicola \par}
       \vspace{0.5cm}
       {\large Gennaio 2026 \par}
       
       \vfill
     \end{titlepage}
     \clearpage
   }
---

# Introduzione

## Il Contesto
L'adozione dell'Intelligenza Artificiale nei processi di agenzia non è più un'opzione, ma una necessità competitiva. Tuttavia, l'uso non regolamentato di questi strumenti comporta rischi significativi, dalla generazione di contenuti non in linea con il brand ("Brand Safety") all'interpretazione errata dei dati.

## Obiettivi del Documento
Questo manuale operativo nasce per uniformare l'utilizzo dell'IA generativa. Gli obiettivi sono:

1.  **Standardizzazione:** Definire prompt replicabili per garantire qualità costante.
2.  **Efficienza:** Ridurre i tempi di "trial and error" nella generazione dei contenuti.
3.  **Affidabilità:** Mitigare le "allucinazioni" dell'IA, specialmente nell'analisi dei dati numerici.

## Struttura dei Moduli
Il manuale è suddiviso in tre aree di competenza:

* **Modulo 1:** Creazione Contenuti (Text Generation)
* **Modulo 2:** Analisi Semantica (Embeddings)
* **Modulo 3:** Analisi Dati Incrociata (Cross-Tabular)