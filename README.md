# ⚔️ ScytheRecon  

**Compact interactive recon tool for Kali Linux.**  
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection, quick subdomain/email harvest and small port scan — all in one run.  
Passive and ethical.

---

## 🧩 Features
- WHOIS lookup  
- DNS & reverse DNS queries  
- HTTP header fingerprinting  
- WAF detection (heuristics)  
- Subdomain & email extraction  
- Quick multi-IP port scan  
- JSON + TXT report output  
- Colorized terminal output

---

## ⚙️ Installation
```bash
git clone https://github.com/TaoTheReaper/scythe-recon.git
cd scythe-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
