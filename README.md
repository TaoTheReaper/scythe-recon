======================== SCYTHE-RECON — ENGLISH ========================

SCYTHE-RECON
Compact interactive reconnaissance tool for Kali Linux.
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection, light subdomain/email harvest and a small port scan — all in one run. Passive and ethical.

OVERVIEW
- Single-file Python tool that runs a recon pipeline and outputs a colorized terminal summary plus report_<domain>.json and optional report_<domain>.txt.
- Intended for learning and authorized defensive recon only.

USAGE (Direct mode - one-shot)
python3 scythe-recon.py -d example.com -o report_example.json -t
Example:
python3 scythe-recon.py -d castellare.it -o report_castellare_it.json -t

FLAGS
-d, --domain     : target domain (required for non-interactive mode)
-o, --output     : output JSON filename (default: report_<domain>.json)
-t, --text       : also create a human-readable .txt report
-v, --verbose    : verbose output (optional)
--timeout SECS   : network timeout seconds (optional)
--no-waf         : skip WAF detection (optional)
--sublist-only   : run only subdomain/email harvest stage (optional)

OUTPUT FILES
report_<domain>.json  -> full structured report (timestamps, raw values, arrays)
report_<domain>.txt   -> simplified human-readable summary
Terminal output -> colorized, column-style summary printed to stdout

COLOR SCHEME (configurable in script)
LABEL_COLOR   = Fore.YELLOW   # field labels
VALUE_COLOR   = Fore.GREEN    # field values
SECTION_COLOR = Fore.CYAN     # section headers / separators
ERROR_COLOR   = Fore.RED
SUCCESS_COLOR = Fore.GREEN
TIP_COLOR     = Fore.MAGENTA
(Change constants at top of scythe-recon.py)

LEGAL & ETHICAL NOTICE
This tool is for educational and defensive purposes only.
- It does NOT exploit vulnerabilities or perform intrusive attacks.
- It performs passive and light active reconnaissance only.
- Use ONLY on domains you own or for which you have explicit written authorization.
- Obtain written permission before testing third-party domains.
- The author disclaims responsibility for misuse.
- Respect local laws, privacy rules and Terms of Service of queried services.

SAFE USE CHECKLIST
- Run inside an isolated environment (Kali VM or sandbox)
- Verify you have written authorization for the target
- Start in passive-only mode (no nmap, --sublist-only)
- Respect robots.txt and source policies
- Keep logs and data under your control
- If in doubt, stop and request permission

SUGGESTED SAFE EXTENSIONS
- Passive subdomain discovery (Amass passive, Subfinder)
- HTTP fingerprint enhancers (WhatWeb, Wappalyzer)
- Optional nmap wrapper behind flag (--nmap) with SAFE defaults (-sS -Pn) — use only with permission
- Exporters: CSV, Markdown, HTML
- Add logging levels and --dry-run

QUICK TROUBLESHOOTING
- Create venv: python3 -m venv .venv && source .venv/bin/activate
- Install deps: pip install -r requirements.txt
- JSON datetime error: use json.dump(report, f, indent=2, ensure_ascii=False, default=str)
- Git push fails: git pull --rebase origin main && git push origin main
- Git conflicts: git status → resolve files → git add <file> → git rebase --continue

REPRODUCIBILITY / INSTALL
git clone https://github.com/TaoTheReaper/scythe-recon.git
cd scythe-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

EXAMPLES
Interactive:
    python3 scythe-recon.py
Direct:
    python3 scythe-recon.py -d example.com -o report_example.json -t

CONTRIBUTION GUIDELINES (short)
- Keep default behavior passive and safe.
- Any active function must be behind an explicit flag and documented.
- Add unit tests for parsing modules (whois/dns/http).
- Document third-party API usage and required API keys.

AUTHOR / LICENSE
Project: SCYTHE-RECON
Author: TaoTheReaper
GitHub: https://github.com/TaoTheReaper
License: MIT — free to use, modify and share with attribution.

======================== SCYTHE-RECON — ITALIANO ========================

SCYTHE-RECON
Strumento compatto di ricognizione interattiva per Kali Linux.
Esegue WHOIS, lookup DNS, fingerprint HTTP, rilevamento WAF, raccolta leggera di sottodomini/email e una piccola scansione porte — tutto in un’unica esecuzione. Passivo ed etico.

SOMMARIO
- Script Python singolo che esegue una pipeline di recon e genera un sommario colorato in terminale più report_<domain>.json e opzionale report_<domain>.txt.
- Destinato a scopi didattici e di difesa (solo test autorizzati).

USO (Modalità Direct - one-shot)
python3 scythe-recon.py -d esempio.it -o report_esempio.json -t
Esempio:
python3 scythe-recon.py -d castellare.it -o report_castellare_it.json -t

FLAG
-d, --domain     : dominio target (obbligatorio in modalità non interattiva)
-o, --output     : nome file JSON di output (default: report_<domain>.json)
-t, --text       : genera anche report leggibile .txt
-v, --verbose    : output dettagliato (opzionale)
--timeout SECS   : timeout rete in secondi (opzionale)
--no-waf         : salta rilevamento WAF (opzionale)
--sublist-only   : esegue solo raccolta sottodomini/email (opzionale)

FILE DI OUTPUT
report_<domain>.json  -> report strutturato completo (timestamp, valori grezzi, array)
report_<domain>.txt   -> riassunto leggibile per umani
Output terminale -> sommario colorato e formattato a colonne

SCHEMA COLORI (configurabile nello script)
LABEL_COLOR   = Fore.YELLOW   # etichette
VALUE_COLOR   = Fore.GREEN    # valori
SECTION_COLOR = Fore.CYAN     # intestazioni / separatori
ERROR_COLOR   = Fore.RED
SUCCESS_COLOR = Fore.GREEN
TIP_COLOR     = Fore.MAGENTA
(Modifica le costanti in cima a scythe-recon.py)

LEGALITÀ & ETICA
Questo strumento è destinato esclusivamente a scopi educativi e difensivi.
- Non sfrutta vulnerabilità né esegue intrusioni.
- Esegue solo ricognizione passiva e check leggeri.
- USARE SOLO su domini di proprietà o con AUTORIZZAZIONE SCRITTA.
- Ottenere permesso scritto prima di testare domini di terzi.
- L’autore declina responsabilità per usi impropri.
- Rispettare leggi locali, privacy e ToS delle sorgenti consultate.

CHECKLIST SICUREZZA
- Esegui in ambiente isolato (VM Kali o sandbox)
- Verifica autorizzazione scritta per il target
- Parti in modalità passive-only (no nmap, --sublist-only)
- Rispetta robots.txt e policy delle sorgenti
- Mantieni log e dati sotto il tuo controllo
- In caso di dubbi, fermati e richiedi autorizzazione

ESTENSIONI CONSIGLIATE (SICURE)
- Amass (modalità passive) o Subfinder per discovery passiva
- WhatWeb o Wappalyzer per fingerprinting avanzato
- Wrapper Nmap opzionale dietro flag (--nmap) con default SAFE (-sS -Pn) — usare solo con permesso
- Export CSV / Markdown / HTML
- Logging migliorato e modalità --dry-run

RISOLUZIONE PROBLEMI RAPIDA
- Virtualenv: python3 -m venv .venv && source .venv/bin/activate
- Dipendenze: pip install -r requirements.txt
- Errore JSON con datetime: usare json.dump(report, f, indent=2, ensure_ascii=False, default=str)
- Push Git fallisce: git pull --rebase origin main && git push origin main
- Conflitti Git: git status → risolvi file → git add <file> → git rebase --continue

INSTALLAZIONE / RIPRODUCIBILITÀ
git clone https://github.com/TaoTheReaper/scythe-recon.git
cd scythe-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

ESEMPI
Interattivo:
    python3 scythe-recon.py
Direct:
    python3 scythe-recon.py -d esempio.it -o report_esempio.json -t

CONTRIBUTION (breve)
- Mantieni comportamento di default passivo e sicuro
- Ogni funzione attiva deve essere dietro flag documentato
- Aggiungi test per moduli di parsing (whois/dns/http)
- Documenta eventuali API esterne e chiavi richieste

AUTORE / LICENZA
Project: SCYTHE-RECON
Author: TaoTheReaper
GitHub: https://github.com/TaoTheReaper
License: MIT — free to use, modify and share with attribution.


