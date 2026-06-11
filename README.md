# NetSentinel-Audit

Asynchronous network auditing tool for rapid vulnerability identification and service mapping.

## Features

- **Asynchronous scanning** (10,000+ ports/second)
- **Service detection** on open ports
- **Vulnerability fingerprinting** (CVEs)
- **Network topology mapping**
- **Export to JSON/CSV** for reporting

## Quick Start

```bash
git clone https://github.com/Mustafa-SeniorDev/netsentinel-audit.git
cd netsentinel-audit
pip install -r requirements.txt
python src/main.py 192.168.1.0/24
```

Scanning Capabilities

Supported Scan Types

Scan Type Description Speed
SYN scan Half-open TCP scanning Fastest
TCP connect Full TCP handshake Slower, more reliable
UDP scan UDP service discovery Slow
ICMP ping Host discovery Very fast

Service Detection

Port Common Service Detection Method
22 SSH Banner grabbing
80 HTTP Request/response
443 HTTPS SSL certificate
3306 MySQL Protocol handshake

Vulnerability Fingerprinting

· Matches service versions against CVE database
· Identifies missing patches and known exploits
· Severity scoring (CVSS 3.1)

Performance

Network Size Scan Time (SYN) Scan Time (TCP)
/24 (256 hosts) 2 minutes 8 minutes
/16 (65k hosts) 30 minutes 2 hours

Example Output

```json
[
  {
    "ip": "192.168.1.10",
    "open_ports": [22, 80, 443],
    "services": {
      "22": "OpenSSH 7.4 (CVE-2017-15906 - Critical)",
      "80": "nginx 1.14.0"
    },
    "vulnerabilities": [
      {
        "cve": "CVE-2017-15906",
        "severity": "CRITICAL",
        "description": "OpenSSH allows arbitrary file overwrite"
      }
    ]
  }
]
```

License

MIT

Author

Mustafa Ramadhani – Senior Quantitative Systems & Data Engineer

