# ⚔️ Scythe-Recon

**Compact interactive reconnaissance tool for Kali Linux.**  
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection, light subdomain/email harvest and a small port scan — all in one run. Passive and ethical.

---

## ENGLISH

### Overview
Single-file Python tool that runs a recon pipeline and prints a colorized terminal summary. It also saves a structured `report_<domain>.json` and an optional human-readable `report_<domain>.txt`. Intended for learning and authorized defensive recon only.

---

### Quick install (Linux / macOS)


git clone https://github.com/<your-user>/scythe-recon.git
cd scythe-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Usage (one-shot / direct)
# interactive:
python3 scythe-recon.py


# direct mode (one-shot):
python3 scythe-recon.py -d example.com -o report_example.json -t
Flags
-d, --domain     : target domain (required for non-interactive mode)
-o, --output     : output JSON filename (default: report_<domain>.json)
-t, --text       : also create a human-readable .txt report
-v, --verbose    : verbose output
--timeout SECS   : network timeout seconds
--no-waf         : skip WAF detection
--sublist-only   : run only subdomain/email harvest stage (passive)
Output files
report_<domain>.json → full structured report (timestamps, raw values, arrays)
report_<domain>.txt → simplified human-readable summary
Terminal output → colorized, column-style summary printed to stdout
Color scheme (configurable)
Change constants at the top of the script (uses colorama):
LABEL_COLOR → Yellow (field labels)
VALUE_COLOR → Green (field values)
SECTION_COLOR → Cyan (section headers / separators)
ERROR_COLOR → Red
SUCCESS_COLOR → Green
TIP_COLOR → Magenta
Legal & ethical (read before use)
This tool is for educational and defensive use only.
It does NOT exploit vulnerabilities or run intrusive attacks.
It performs passive and light active recon only.
Use only on domains you own or where you have explicit written authorization.
Obtain written permission before testing third-party domains.
Respect local laws, privacy rules and Terms of Service.
The project author disclaims responsibility for misuse.
Safe checklist
Run inside an isolated environment (Kali VM or sandbox).
Start with passive-only options (no nmap) until you have permission.
Keep logs and data under your control.
If in doubt, stop and get permission.
Suggested safe extensions
Passive subdomain discovery: Amass (passive), Subfinder
HTTP fingerprinting: WhatWeb / Wappalyzer (local or API)
Optional Nmap wrapper behind --nmap flag (default safe flags) — use only with permission
Exporters: CSV, Markdown, HTML
Add logging levels and --dry-run mode
Troubleshooting quick tips
Virtualenv: python3 -m venv .venv && source .venv/bin/activate
Install deps: pip install -r requirements.txt
JSON datetime issue: ensure json.dump(..., default=str) when writing reports
Git push error (remote has content): git pull --rebase origin main && git push origin main
Examples
# Interactive mode:
python3 scythe-recon.py

# Direct:
python3 scythe-recon.py -d castellare.it -o report_castellare_it.json -t
Contribution guidelines (short)
Keep default behavior passive and safe.
Any active scanning must be behind an explicit flag and documented.
Add unit tests for parsing functions (whois/dns/http).
Document external APIs and required API keys.
License & project
Project: Scythe-Recon
GitHub: https://github.com/<your-user>/scythe-recon
License: MIT — free to use, modify and share with attribution.
ITALIANO
Panoramica
Script Python singolo che esegue una pipeline di ricognizione, stampa un sommario colorato in terminale e salva report_<domain>.json (strutturato) e opzionalmente report_<domain>.txt. Destinato a scopi didattici e difensivi: solo test autorizzati.
Installazione rapida (Linux / macOS)
git clone https://github.com/<tuo-utente>/scythe-recon.git
cd scythe-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Uso (direct / one-shot)
# interattivo:
python3 scythe-recon.py

# modalità diretta:
python3 scythe-recon.py -d esempio.it -o report_esempio.json -t
Flag
-d, --domain     : dominio target (obbligatorio in modalità non interattiva)
-o, --output     : nome file JSON di output (default: report_<domain>.json)
-t, --text       : genera anche report leggibile .txt
-v, --verbose    : output dettagliato
--timeout SECS   : timeout rete in secondi
--no-waf         : salta rilevamento WAF
--sublist-only   : esegue solo raccolta sottodomini/email (passiva)
File di output
report_<domain>.json → report strutturato completo
report_<domain>.txt → riassunto leggibile
Output terminale → sommario colorato a colonne
Schema colori (configurabile)
Modificare le costanti in cima allo script (usa colorama):
LABEL_COLOR → Giallo
VALUE_COLOR → Verde
SECTION_COLOR → Ciano
ERROR_COLOR → Rosso
SUCCESS_COLOR → Verde
TIP_COLOR → Magenta
Legalità & etica (leggilo)
Strumento solo per scopi educativi e difensivi.
Non sfrutta vulnerabilità né esegue intrusioni.
Esegue ricognizione passiva e controlli leggeri.
Usa solo su domini di tua proprietà o con autorizzazione scritta.
Rispettare leggi locali, privacy e ToS.
Checklist sicurezza
Esegui in VM o sandbox.
Parti in modalità passive-only (no nmap) se non hai permesso esplicito.
Tieni sotto controllo log e dati.
In caso di dubbi, fermati.
Estensioni consigliate (sicure)
Amass (passive), Subfinder per discovery passiva
WhatWeb / Wappalyzer per fingerprinting avanzato
Wrapper Nmap opzionale dietro flag (--nmap) con default SAFE — solo con permesso
Export CSV / Markdown / HTML
Logging avanzato e --dry-run
Risoluzione problemi rapida
Virtualenv: python3 -m venv .venv && source .venv/bin/activate
Dipendenze: pip install -r requirements.txt
Problema JSON con datetime: json.dump(..., default=str)
Errore Git push: git pull --rebase origin main && git push origin main
Esempi
# Interattivo:
python3 scythe-recon.py

# Direct:
python3 scythe-recon.py -d castellare.it -o report_castellare_it.json -t
Contributi (breve)
Mantieni comportamento di default passivo e sicuro.
Ogni funzione attiva deve essere dietro flag documentato.
Aggiungi test per parsing (whois/dns/http).
Documenta API esterne e chiavi.
Licenza & progetto
Project: Scythe-Recon
GitHub: https://github.com/<your-user>/scythe-recon
License: MIT
FINE — copia e incolla tutto questo in README.md. Vuoi che:
lo carichi direttamente sul repo (ti do i comandi git add/commit/push) per il Mac?
oppure preferisci che generi anche un README.pdf o README.txt scaricabile? Dimmelo e ti do i comandi esatti.
