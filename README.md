============================================================
SCYTHE-RECON - by TaoTheReaper
============================================================

Compact interactive reconnaissance tool for Kali Linux.
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection,
quick subdomain/email harvest and small port scan — all in one run.
Passive and ethical.

------------------------------------------------------------
FEATURES
------------------------------------------------------------
- WHOIS lookup
- DNS & reverse DNS queries
- HTTP header fingerprinting
- WAF detection (heuristics)
- Subdomain & email extraction
- Quick multi-IP port scan
- JSON + TXT report output
- Colorized terminal output

------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------
Tested on Python 3.10+
Dependencies (see requirements.txt):
    python-whois
    dnspython
    requests
    beautifulsoup4
    python-dateutil
    colorama

------------------------------------------------------------
INSTALLATION (Linux / macOS)
------------------------------------------------------------
1. Clone the repository:
       git clone https://github.com/TaoTheReaper/scythe-recon.git
       cd scythe-recon

2. Create virtual environment:
       python3 -m venv .venv
       source .venv/bin/activate

3. Install dependencies:
       pip install -r requirements.txt

------------------------------------------------------------
USAGE
------------------------------------------------------------

INTERACTIVE MODE:
    python3 scythe-recon.py
    → then enter the target domain when prompted
      (example: castellare.it)

DIRECT MODE:
    python3 scythe-recon.py -d example.com -o report.json -t

FLAGS:
    -d, --domain   : Target domain (required for non-interactive mode)
    -o, --output   : Output file name (default: report_<domain>.json)
    -t, --text     : Also create a human-readable TXT report
    -v, --verbose  : Verbose output (optional)

EXAMPLES:
    python3 scythe-recon.py
    python3 scythe-recon.py -d castellare.it -o report_castellare.json -t

------------------------------------------------------------
OUTPUT FILES
------------------------------------------------------------
    report_<domain>.json  → full structured report
    report_<domain>.txt   → simplified text report
    The terminal output is colorized by section for readability.

------------------------------------------------------------
COLOR SCHEME
------------------------------------------------------------
Labels: Yellow
Values: Green
Sections: Cyan
Editable in scythe-recon.py using colorama constants:
    LABEL_COLOR = Fore.YELLOW
    VALUE_COLOR = Fore.GREEN
    SEPARATOR_COLOR = Fore.CYAN

------------------------------------------------------------
LEGAL & ETHICAL NOTICE
------------------------------------------------------------
This tool is designed for educational and defensive use only.
- It does NOT exploit vulnerabilities or perform intrusive scans.
- Use only on domains you own or have explicit written authorization to test.
- The author (TaoTheReaper) declines all responsibility for misuse.
- Always comply with laws and professional ethics.

------------------------------------------------------------
SAFE USE CHECKLIST
------------------------------------------------------------
✓ Run inside your Kali VM or test environment
✓ Avoid unauthorized targets
✓ Respect Terms of Service and data access policies
✓ Keep your recon passive

------------------------------------------------------------
EXTENDING THE TOOL (Optional ideas)
------------------------------------------------------------
- Integrate Amass or Subfinder for passive subdomain discovery
- Use WhatWeb or Wappalyzer APIs for deeper fingerprinting
- Add optional Nmap wrapper (safe -Pn or -sS only, with consent)
- Add CSV or Markdown report exporters
- Improve logging & verbosity options

------------------------------------------------------------
AUTHOR
------------------------------------------------------------
Created by: TaoTheReaper
GitHub: https://github.com/TaoTheReaper

------------------------------------------------------------
LICENSE
------------------------------------------------------------
MIT License
Free to use, modify and share with attribution.

------------------------------------------------------------
ITALIANO
------------------------------------------------------------
Scythe-Recon è uno strumento compatto per la ricognizione passiva e legale.
Esegue WHOIS, query DNS, fingerprint HTTP, rilevamento WAF, raccolta email
e sottodomini, e una piccola scansione porte.

Installazione:
    git clone https://github.com/TaoTheReaper/scythe-recon.git
    cd scythe-recon
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Utilizzo:
    python3 scythe-recon.py
    oppure
    python3 scythe-recon.py -d esempio.it -o report.json -t

Usare solo su domini di proprietà o con autorizzazione esplicita.
Tutte le azioni sono passive e legali.


