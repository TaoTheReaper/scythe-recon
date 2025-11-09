#!/usr/bin/env python3
# recon_kali.py - palette aggiornata: labels=green, values=yellow, sections=cyan, notes=orange

import json, re, socket, sys, time
from datetime import datetime, timezone
import concurrent.futures

from colorama import Fore, Back, Style, init as colorama_init
colorama_init(autoreset=True)

# external libs
try:
    import whois
    import dns.resolver
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print(Fore.RED + "Missing libraries. Install inside .venv:")
    print("  pip install python-whois dnspython requests beautifulsoup4 colorama")
    sys.exit(1)

USER_AGENT = "ReconKali/column/1.0"
TIMEOUT = 8

TECH_PATTERNS = {
    "WordPress": [r"wp-content", r"wp-includes", r"wp-"],
    "Cloudflare": [r"cloudflare", r"CF-Ray", r"cf-request-id"],
    "nginx": [r"nginx"],
    "Apache": [r"Apache"],
    "IIS": [r"Microsoft-IIS"],
    "PHP": [r"PHP/"],
}

WAF_SIGS = {
    "headers": [r"cloudflare", r"incapsula", r"akamai", r"imperva", r"f5", r"sucuri", r"ddos-guard", r"fastly"],
    "cookies": [r"__cfduid", r"__cfruid", r"visid_incap", r"incap_ses"]
}

SUBDOMAIN_WORDLIST = ["www","mail","ftp","admin","dev","api","shop","portal","beta","staging","blog","smtp","webmail"]

# ---------- network helpers ----------
def http_get(url):
    try:
        return requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT, allow_redirects=True)
    except:
        return None

def run_whois(domain):
    out = {}
    try:
        w = whois.whois(domain)
        out['registrar'] = w.registrar
        out['creation_date'] = w.creation_date
        out['expiration_date'] = w.expiration_date
        out['name_servers'] = w.name_servers
        out['emails'] = w.emails
    except Exception as e:
        out['error'] = str(e)
    return out

def dns_queries(domain):
    res = {}
    for t in ["A","AAAA","MX","NS","TXT","CNAME","SOA"]:
        try:
            answers = dns.resolver.resolve(domain, t, lifetime=5)
            res[t] = [a.to_text() for a in answers]
        except Exception:
            res[t] = []
    return res

def reverse_dns(ips):
    out = {}
    for ip in ips:
        try:
            out[ip] = socket.gethostbyaddr(ip)[0]
        except Exception:
            out[ip] = None
    return out

def fingerprint_http(domain):
    info = {"http":None, "https":None, "technologies":[]}
    for scheme in ("http://","https://"):
        url = f"{scheme}{domain}"
        r = http_get(url)
        key = "https" if scheme=="https://" else "http"
        if r:
            txt = (r.text or "") + " ".join([str(v) for v in r.headers.values()])
            info[key] = {"status": r.status_code, "server": r.headers.get("Server"), "title": None}
            try:
                soup = BeautifulSoup(r.text, "html.parser")
                info[key]["title"] = soup.title.string.strip() if soup.title and soup.title.string else None
            except Exception:
                pass
            for name,pats in TECH_PATTERNS.items():
                for p in pats:
                    if re.search(p, txt, re.I) and name not in info["technologies"]:
                        info["technologies"].append(name)
        else:
            info[key] = None
    return info

def detect_waf(domain):
    r = http_get(f"https://{domain}")
    if not r:
        return []
    wafs = []
    for sig in WAF_SIGS["headers"]:
        for v in r.headers.values():
            if re.search(sig, str(v), re.I):
                wafs.append(sig)
    if re.search(r"cloudflare", str(r.headers), re.I):
        wafs.append("cloudflare")
    return list(dict.fromkeys(wafs))

def harvest_basic(domain):
    out = {"emails":[], "subdomains":[]}
    r = http_get(f"https://{domain}") or http_get(f"http://{domain}")
    if r and r.text:
        for m in re.findall(r"mailto:([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+)", r.text, re.I):
            out["emails"].append(m)
        for m in re.findall(r"([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+)", r.text, re.I):
            out["emails"].append(m)
    out["emails"] = sorted(list(set(out["emails"])))
    def try_sub(w):
        fqdn = f"{w}.{domain}"
        try:
            answers = dns.resolver.resolve(fqdn, "A", lifetime=2)
            ips = [a.to_text() for a in answers]
            return (fqdn, ips)
        except Exception:
            return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        futures = [ex.submit(try_sub, w) for w in SUBDOMAIN_WORDLIST]
        for f in concurrent.futures.as_completed(futures):
            r = f.result()
            if r:
                out["subdomains"].append(r[0])
    return out

def quick_port_scan(ips, ports=(80,443,22,25,3306,3389,8080)):
    scan = {}
    for ip in ips:
        scan[ip] = {}
        for p in ports:
            s = socket.socket()
            s.settimeout(0.7)
            try:
                s.connect((ip, p))
                scan[ip][str(p)] = "open"
                s.close()
            except Exception:
                scan[ip][str(p)] = "closed"
    return scan

# ---------- pretty column printer ----------
# palette per tua richiesta:
# - etichette (LBL) = GREEN
# - valori (VAL) = YELLOW
# - sezioni / separatori (SEC) = CYAN
# - tecnologie (TECH) = MAGENTA
# - waf (WAFC) = RED
# - note/testi minori (NOTE) = arancio approx (LIGHTRED_EX)
LBL = Fore.GREEN
VAL = Fore.YELLOW
SEC = Fore.CYAN
TECH = Fore.MAGENTA
WAFC = Fore.RED
NOTE = Fore.LIGHTRED_EX + Style.BRIGHT  # "arancione" approssimato

def print_section_title(title):
    print(SEC + "\n" + "="*60)
    print(SEC + f" {title}")
    print(SEC + "="*60 + Style.RESET_ALL)

def print_label_col(label, value_lines):
    print(LBL + f"{label}:" + Style.RESET_ALL)
    if not value_lines:
        print("  " + VAL + "(none)" + Style.RESET_ALL)
        return
    for v in value_lines:
        if isinstance(v, list):
            for item in v:
                for line in str(item).splitlines():
                    print("  " + VAL + line + Style.RESET_ALL)
        else:
            for line in str(v).splitlines():
                print("  " + VAL + line + Style.RESET_ALL)

def pretty_report(report):
    print(SEC + "\n" + "="*60)
    h = f"Mini report for: {report['domain']}  |  Generated: {report['timestamp']}"
    print(VAL + h + Style.RESET_ALL)  # header in value color for contrast
    print(SEC + "="*60 + Style.RESET_ALL)

    print_section_title("WHOIS")
    who = report.get("whois", {})
    print_label_col("Registrar", [who.get("registrar")])
    creation = who.get("creation_date")
    expiry = who.get("expiration_date")
    def fmt_dates(d):
        if d is None: return None
        if isinstance(d, (list, tuple)):
            return [str(x) for x in d]
        return [str(d)]
    print_label_col("Creation", fmt_dates(creation))
    print_label_col("Expiry", fmt_dates(expiry))

    print_section_title("DNS")
    dns = report.get("dns", {})
    print_label_col("A records", dns.get("A"))
    print_label_col("AAAA", dns.get("AAAA"))
    print_label_col("NS", dns.get("NS"))
    print_label_col("MX", dns.get("MX"))
    print_label_col("TXT", dns.get("TXT"))

    print_section_title("HTTP & Technologies")
    techs = report.get("http",{}).get("technologies") or []
    if techs:
        print(LBL + "Technologies detected:" + Style.RESET_ALL)
        for t in techs:
            print("  " + TECH + t + Style.RESET_ALL)
    else:
        print_label_col("Technologies detected", [])

    waf = report.get("waf") or []
    print_section_title("WAF")
    if waf:
        for w in waf:
            print("  " + WAFC + w + Style.RESET_ALL)
    else:
        print_label_col("Likely", [])

    print_section_title("Harvest (emails / subdomains)")
    harvest = report.get("harvest", {})
    print_label_col("Emails", harvest.get("emails"))
    print_label_col("Subdomains", harvest.get("subdomains"))

    print_section_title("Network")
    rev = report.get("reverse_dns") or {}
    print_label_col("Reverse DNS", [f"{k} -> {v}" for k,v in rev.items()])
    ports = report.get("ports") or {}
    print_label_col("Port scan (quick)", [f"{ip}: {', '.join([p+':'+s for p,s in v.items()])}" for ip,v in ports.items()])

    print(SEC + "\n" + "="*60 + Style.RESET_ALL)

# ---------- main ----------
def main():
    print(SEC + "\n=== Recon Kali - Column view (color) ===" + Style.RESET_ALL)
    domain = input(NOTE + "Enter domain (example.com): " + Style.RESET_ALL).strip()
    if not domain:
        print(WAFC + "No domain provided. Exiting." + Style.RESET_ALL)
        return

    report = {"domain":domain, "timestamp": datetime.now(timezone.utc).isoformat()}
    print(NOTE + "[*] WHOIS ..." + Style.RESET_ALL)
    report["whois"] = run_whois(domain)
    print(NOTE + "[*] DNS queries ..." + Style.RESET_ALL)
    report["dns"] = dns_queries(domain)

    ips = []
    for ip in report["dns"].get("A",[]):
        ips.append(ip.split()[0])
    for ip in report["dns"].get("AAAA",[]):
        ips.append(ip.split()[0])
    ips = list(dict.fromkeys(ips))

    print(NOTE + f"    found IPs: {ips}" + Style.RESET_ALL)
    print(NOTE + "[*] Reverse DNS ..." + Style.RESET_ALL)
    report["reverse_dns"] = reverse_dns(ips)

    print(NOTE + "[*] HTTP fingerprint ..." + Style.RESET_ALL)
    report["http"] = fingerprint_http(domain)

    print(NOTE + "[*] WAF detection ..." + Style.RESET_ALL)
    report["waf"] = detect_waf(domain)

    print(NOTE + "[*] Harvest (emails + subdomains) ..." + Style.RESET_ALL)
    report["harvest"] = harvest_basic(domain)

    print(NOTE + "[*] Quick port scan ..." + Style.RESET_ALL)
    report["ports"] = quick_port_scan(ips)

    fname = f"report_{domain.replace('.', '_')}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    print(Fore.GREEN + f"\n✅ Recon completed. Report saved: {fname}" + Style.RESET_ALL)
    pretty_report(report)

if __name__ == "__main__":
    main()
