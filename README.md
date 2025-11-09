# ⚔️ SCYTHE-RECON

**Compact interactive reconnaissance tool for Kali Linux.**  
Performs WHOIS, DNS lookups, HTTP fingerprinting, WAF detection, quick subdomain/email harvest and a small port scan — all in one run.  
Passive and ethical by design.

---

## 🧩 Overview

SCYTHE-RECON automates the initial reconnaissance phase of penetration testing and OSINT operations.  
It collects key network and domain information in a single, lightweight execution — designed for speed, simplicity, and clean reports.

---

## 🚀 Features

- WHOIS lookup  
- DNS & reverse DNS queries  
- HTTP header fingerprinting  
- WAF detection (heuristics)  
- Subdomain & email extraction  
- Quick multi-IP port scan  
- JSON + TXT report output

---

## 🧠 Usage

### Basic Command
```bash
python3 scythe-recon.py -t target.com
