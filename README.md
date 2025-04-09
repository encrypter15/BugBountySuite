# BugBountySuite

**BugBountySuite**—Hunter’s Hub: the ultimate bug bounty toolkit. Recon, vuln tracking, and scope scraping—all in one slick package.

## Features
- **Target Management**: Organize your bounty targets—scope’s king.
- **Vulnerability Tracking**: Log vulns with PoC, severity, status—full detail.
- **Recon Tools**: 
  - **BugWatch**: Asset discovery—github.com/encrypter15/BugBountySuite/BugWatch
  - **VulnVoyager**: Adaptive vuln hunter—github.com/encrypter15/BugBountySuite/VulnVoyager
  - **SubSonic**: Subdomain beast—github.com/encrypter15/BugBountySuite/SubSonic
  - **BugBountyScraper**: Scope scraper (HackerOne, Bugcrowd, Bugbounter, YesWeHack, Intigriti)—github.com/encrypter15/BugBountySuite/BugBountyScraper
  - **Nmap**: Port scanning OG—nmap.org
  - **Amass**: OWASP’s DNS enumerator—github.com/OWASP/Amass
- **GUI Power**: PyQt6-driven—click your way to glory.

## Installation
1. Clone this beast:
   ```bash
   git clone https://github.com/encrypter15/BugBountySuite.git
   cd BugBountySuite
   ```
2. Install the juice:
   ```bash
   pip install -r requirements.txt
   ```
3. Install system tools:
   - Nmap: `sudo apt install nmap`
   - Amass: `go install github.com/OWASP/Amass/v3/...@latest`

## Usage
**GUI**:
```bash
python main.py
```
- Click "Add Target", "Run Recon Tools"—go wild!

**CLI**:
```bash
python main.py --target example.com --scan
```

## Ethical Use
Only hit legit targets—don’t be a jailbird, you clever hunter.

## License
MIT—free as the wind. See `LICENSE`.

*Author:* encrypter15, bug bounty legend.  
*Version:* 1.1—born to dominate.
