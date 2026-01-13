import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- CONFIGURAZIONE DINAMICA ---
SOURCE_DIR = os.path.join("Content", "Sources")
OUTPUT_DIR = os.path.join("Content", "TranslatedAPI")
ALLOWED_EXTENSIONS = {'.txt', '.md'} # Filtro per evitare file nascosti o spazzatura

def clean_content(text):
    """NormalizzazioneRegex"""
    text = re.sub(r'<(Notice|CodeSample|IconItem).*?>.*?</\1>', '', text, flags=re.DOTALL)
    text = re.sub(r'\[(.*?)\]\(/docs/.*?\)', r'\1', text)
    return text.strip()

def ai_translate_and_adapt(text):
    """Trasformazione semantica tramite GPT-4o"""
    prompt_sistema = (
        "Sei un Senior Editor. Traduci in italiano, adatta il contenuto in un linguaggio non tecnico e "
        "coerente con il contesto aziendale.Poni maggiore attenzione al prompt engineering  applicato a text generation, language detection, e cross-tabular analysis."
         " Garantisci COERENZA GRAFICA: "
        "Titoli con # e ##, esempi in blockquote (>), liste puntate. Formato Markdown."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": text}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Errore API: {e}")
        return None

def main():
    print("--- AVVIO WORKFLOW UNIVERSALE ---")
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    # LETTURA AUTOMATICA E ORDINATA DELLA CARTELLA SORGENTE
    # Usiamo sorted() per essere sicuri che l'indice 00, 01 segua l'ordine alfabetico dei file sorgente
    files = sorted([f for f in os.listdir(SOURCE_DIR) if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS])
    
    if not files:
        print(f"Nessun file trovato in {SOURCE_DIR}")
        return

    print(f"Trovati {len(files)} file da elaborare.")

    # Aggiungiamo 'enumerate' per avere un indice (i) che parte da 0
    for i, filename in enumerate(files): 
        src_path = os.path.join(SOURCE_DIR, filename)
        
        #PREFISSO NUMERICO ---
        target_name = f"{i:02d}_{os.path.splitext(filename)[0]}.md"
        target_path = os.path.join(OUTPUT_DIR, target_name)

        print(f"Processando: {filename} -> {target_name}...")
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Step 1: Pulizia
        clean_text = clean_content(content)
        
        # Step 2: IA
        result = ai_translate_and_adapt(clean_text)
        
        final_output = result if result else clean_text
        
        with open(target_path, "w", encoding="utf-8") as f_out:
            f_out.write(final_output)
            
    print("--- WORKFLOW COMPLETATO ---")
if __name__ == "__main__":
    main()