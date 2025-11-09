SCYTHE-RECON
Compact interactive reconnaissance tool for Kali Linux.
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection, quick subdomain/email harvest and
a small port scan — all in one run.
Passive and ethical.
FEATURES
- WHOIS lookup
- DNS & reverse DNS queries
- HTTP header fingerprinting
- WAF detection (heuristics)
- Subdomain & email extraction
- Quick multi-IP port scan
- JSON + TXT report output
- Colorized terminal output
REQUIREMENTS
Tested on Python 3.10+
Dependencies (see requirements.txt):
python-whois, dnspython, requests, beautifulsoup4, python-dateutil, colorama
INSTALLATION (Linux / macOS)
1. Clone the repository:
git clone https://github.com/TaoTheReaper/scythe-recon.git
cd scythe-recon
2. Create virtual environment:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt
USAGE
Interactive mode:
python3 scythe-recon.py
Direct mode:
python3 scythe-recon.py -d example.com -o report.json -t
FLAGS
-d, --domain : target domain (required for non-interactive)
-o, --output : output file name (default: report_.json)
-t, --text : also create human-readable .txt report
-v, --verbose : verbose output (optional)
OUTPUT FILES
- report_.json -> full structured report
- report_.txt -> simplified text report
COLOR SCHEME
Labels: Yellow
Values: Green
Sections: Cyan
LEGAL & ETHICAL NOTICE
This tool is designed for educational and defensive use only.
- It does NOT exploit vulnerabilities or perform intrusive scans.
- Use only on domains you own or have explicit written authorization to test.
- The author (TaoTheReaper) declines all responsibility for misuse.
- Always comply with laws and professional ethics.
SAFE USE CHECKLIST
- Run inside your Kali VM or a controlled test environment
- Avoid unauthorized targets
- Respect Terms of Service and data access policies
- Keep your recon passive
EXTENDING THE TOOL (optional ideas)
- Integrate Amass or Subfinder for passive subdomain discovery
- Use WhatWeb or Wappalyzer APIs for deeper fingerprinting
- Add optional Nmap wrapper (safe -Pn or -sS only, with consent)
- Add CSV/Markdown exporters
AUTHOR
Created by: TaoTheReaper
GitHub: https://github.com/TaoTheReaper
LICENSE
MIT License — free to use, modify and share with attribution.
