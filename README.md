# ⚔️ SCYTHE-RECON

A swift, all-in-one reconnaissance script for a quick and colorful overview of any domain.
It wraps up WHOIS, DNS, web fingerprinting, and more into a single, fast execution. Designed for clarity and efficiency.

## 🧩 Overview

SCYTHE-RECON is your first step in any security assessment or OSINT investigation. It quickly gathers essential public information about a domain and presents it in a clean, color-coded terminal view. No complex setup, just one script to get a solid initial footprint, with a handy JSON report saved for later.

## 🚀 Features

-   📜 **WHOIS Lookup**: Fetches registrar, creation, and expiry dates.
-   🌐 **DNS Enumeration**: Scans for A, AAAA, MX, NS, and TXT records.
-   👈 **Reverse DNS**: Finds hostnames for the target's IP addresses.
-   💻 **Web Technology Detection**: Identifies servers (nginx, Apache), frameworks (WordPress), and services (Cloudflare).
-   🛡️ **WAF Detection**: Checks for common Web Application Firewalls protecting the site.
-   📬 **Email & Subdomain Discovery**: Finds public emails on the homepage and discovers common subdomains.
-   🚪 **Quick Port Scan**: Checks the status of essential network ports (HTTP, HTTPS, SSH, etc.).
-   🎨 **Colorful Terminal Output**: Makes the report easy to read at a glance.
-   💾 **JSON Report**: Saves all findings to a `report_{domain}.json` file for later use.

## ⚙️ Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/taothereaper/scythe-recon.git
    cd scythe-recon
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install python-whois dnspython requests beautifulsoup4 colorama
    ```

## 🎯 How to Run

Just execute the script. It will prompt you for the domain to analyze.

```sh
python3 scythe-recon.py
```

➡️ **Input:** `Enter domain (example.com): example.com`

The results will be displayed live in the terminal, and a `report_example_com.json` file will be waiting for you in the same folder.

## ⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only. Don't use it for shady stuff. You are responsible for your own actions.






# ⚔️ SCYTHE-RECON 

Uno script di ricognizione rapido e all-in-one per una panoramica immediata e colorata di qualsiasi dominio.
Unisce WHOIS, DNS, fingerprinting web e altro in un'unica, veloce esecuzione. Progettato per essere chiaro ed efficiente.

## 🧩 Panoramica

SCYTHE-RECON è il tuo primo passo in qualsiasi valutazione di sicurezza o indagine OSINT. Raccoglie rapidamente le informazioni pubbliche essenziali su un dominio e le presenta in una vista pulita e colorata sul terminale. Nessuna configurazione complessa, solo uno script per ottenere un solido footprint iniziale, con un comodo report JSON salvato per dopo.

## 🚀 Funzionalità

-   📜 **Dati WHOIS**: Recupera registrar, date di creazione e scadenza.
-   🌐 **Enumerazione DNS**: Cerca record A, AAAA, MX, NS e TXT.
-   👈 **DNS Inverso**: Trova i nomi host associati agli IP del target.
-   💻 **Rilevamento Tecnologie Web**: Identifica server (nginx, Apache), framework (WordPress) e servizi (Cloudflare).
-   🛡️ **Rilevamento WAF**: Verifica la presenza dei più comuni Web Application Firewall a protezione del sito.
-   📬 **Scoperta di Email e Sottodomini**: Trova email pubbliche sulla homepage e scopre i sottodomini più comuni.
-   🚪 **Scansione Rapida delle Porte**: Controlla lo stato delle porte di rete essenziali (HTTP, HTTPS, SSH, ecc.).
-   🎨 **Output Colorato nel Terminale**: Rende il report facile da leggere a colpo d'occhio.
-   💾 **Report in JSON**: Salva tutti i risultati in un file `report_{dominio}.json` per un uso futuro.

## ⚙️ Installazione

1.  **Clona la repository:**
    ```sh
    git clone https://github.com/taothereaper/scythe-recon.git
    cd scythe-recon
    ```

2.  **Crea un ambiente virtuale (consigliato):**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Installa le dipendenze:**
    ```sh
    pip install python-whois dnspython requests beautifulsoup4 colorama
    ```

## 🎯 Come si Usa

Esegui semplicemente lo script. Ti chiederà di inserire il dominio da analizzare.

```sh
python3 scythe-recon.py
```

➡️ **Input:** `Enter domain (example.com): example.com`

I risultati verranno mostrati in tempo reale nel terminale e un file `report_example_com.json` ti aspetterà nella stessa cartella.

## ⚠️ Disclaimer

Questo strumento è destinato esclusivamente a scopi didattici e a test di sicurezza autorizzati. Non usarlo per attività losche. Sei responsabile delle tue azioni.
