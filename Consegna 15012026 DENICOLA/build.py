import subprocess
import os
import sys

# --- CONFIGURAZIONE PROGETTO ---

# Nome base per i file finali
OUTPUT_FILENAME = "Manuale_Operativo_IA"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "Content", "Translated")
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
STYLE_FILE = os.path.join(BASE_DIR, "style.css") 
EPUB_CSS_FILE = os.path.join(BASE_DIR, "epub.css")

files_in_dir = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")]
MD_FILES = sorted(files_in_dir)

# percorsi completi per pandoc
SOURCE_PATHS = [os.path.join(SOURCE_DIR, f) for f in MD_FILES]

def ensure_output_dir():
    """Crea la cartella Output se non esiste"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Creata cartella di output: {OUTPUT_DIR}")

def check_pandoc():
    try:
        subprocess.run(["pandoc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Pandoc rilevato. Inizio build...")
    except FileNotFoundError:
        print("ERRORE CRITICO: Pandoc non trovato nel sistema.")
        sys.exit(1)

def check_source_files():
    """Verifica che tutti i file markdown esistano prima di partire"""
    missing = []
    for f in SOURCE_PATHS:
        if not os.path.exists(f):
            missing.append(f)
    
    if missing:
        print("ERRORE: Impossibile trovare i seguenti file nella cartella Translated:")
        for m in missing:
            print(f"   - {m}")
        print("Verifica i nomi dei file o la struttura delle cartelle.")
        sys.exit(1)

def run_pandoc(output_format, extension, extra_args=[]):
    output_file_path = os.path.join(OUTPUT_DIR, f"{OUTPUT_FILENAME}.{extension}")
    print(f"Generazione {output_format.upper()}...")
    
    command = [
        "pandoc",
        *SOURCE_PATHS,
        "-o", output_file_path,
        "--toc",
        "--toc-depth=2",
        "-s",
        *extra_args
    ]
    
    try:
        subprocess.run(command, check=True, capture_output=True)
        print(f"Creato: {output_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la creazione del {output_format}:")
     
        err_msg = e.stderr.decode('utf-8') if e.stderr else "Errore sconosciuto"
        print(err_msg)

# --- MAIN ---
def main():
    print(f"Avvio build system. Directory sorgente: {SOURCE_DIR}")
    check_pandoc()
    check_source_files()
    ensure_output_dir()
    print("-" * 40)

    # 1. HTML (Usa style.css)
    css_arg = ["--css", STYLE_FILE] if os.path.exists(STYLE_FILE) else []
    if not css_arg:
        print("style.css non trovato.")
    
    run_pandoc("html", "html", [*css_arg, "--metadata", "title=Manuale Operativo IA"])

    # 2. EPUB (Usa ePub.css se disponibile, sennò style.css)
    if os.path.exists(EPUB_CSS_FILE):
        epub_css_arg = ["--css", EPUB_CSS_FILE]
    else:
        # Fallback se non trova il file
        epub_css_arg = []

    epub_extra_args = [
        *epub_css_arg,
        "--metadata", "title=Manuale Operativo IA",
        "--metadata", "titlepage=false" 
    ]
    
    run_pandoc("epub", "epub", epub_extra_args)

    # 3. PDF (LaTeX)
    run_pandoc("pdf", "pdf", ["--pdf-engine=xelatex"])

    print("-" * 40)
    print("Build completata.")

if __name__ == "__main__":
    main()