import os
import re

# --- CONFIGURAZIONE PERCORSI (Secondo LT6) ---
SOURCE_DIR = os.path.join("Content", "Sources")
# Creiamo una cartella intermedia per i file puliti prima dell'IA
CLEAN_DIR = os.path.join("Content", "Cleaned")

def raw_cleaning(text):
    """
    Esegue la pulizia deterministica del testo (Normalizzazione).
    Obiettivo: Interoperabilità
    """
    # 1. Rimozione tag JSX/React (es. <Notice>, <CodeSample>)
    text = re.sub(r'<(Notice|CodeSample|IconItem).*?>.*?</\1>', '', text, flags=re.DOTALL)
    
    # 2. Rimozione di tag di apertura/chiusura rimasti orfani
    text = re.sub(r'<[^>]+>', '', text)
    
    # 3. Pulizia link proprietari (trasforma [testo](/docs/...) in solo 'testo')
    text = re.sub(r'\[(.*?)\]\(/docs/.*?\)', r'\1', text)
    
    # 4. Normalizzazione degli spazi e delle linee vuote eccessive
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

def main():
    print("--- AVVIO PULIZIA ROZZA (Pre-processing) ---")
    
    if not os.path.exists(CLEAN_DIR):
        os.makedirs(CLEAN_DIR)

    # Scansione dinamica della cartella Sources
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(('.txt', '.md'))]
    
    for filename in files:
        src_path = os.path.join(SOURCE_DIR, filename)
        # Forziamo l'estensione .md per la portabilità
        target_name = os.path.splitext(filename)[0] + ".md"
        target_path = os.path.join(CLEAN_DIR, target_name)
        
        print(f"Pulizia di: {filename}...")
        
        try:
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Esecuzione della pulizia
            cleaned_text = raw_cleaning(content)
            
            with open(target_path, "w", encoding="utf-8") as f_out:
                f_out.write(cleaned_text)
                
        except Exception as e:
            print(f"Errore su {filename}: {e}")

    print(f"--- COMPLETATO: File puliti pronti in {CLEAN_DIR} ---")

if __name__ == "__main__":
    main()