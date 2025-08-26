#OPEN SOURCE MINI PROJECT TCP SYN Port Scanner (Scapy)

This project is a lightweight TCP SYN port scanner built using [Scapy](https://scapy.readthedocs.io/en/latest/).  
It detects **OPEN**, **CLOSED**, and **FILTERED** ports on alive hosts and logs the results into a file.  

---

## 📌 Features
- Reads alive hosts from a file (`alive_hosts.txt`).
- Scans selected ports (`22`, `80`, `443` by default).
- Identifies ports as **OPEN**, **CLOSED**, or **FILTERED**.
- Sends RST packets to gracefully close connections.
- Saves results in `port_scan_results.txt`.

---
Requirements:

Python 3.8+

Scapy(Library)

Root/Administrator privileges (required for raw packet operations)

1) Install requirements:
 pip install scapy

2) Add Hosts:(Edit alive_hosts.txt with one IP address per line)
192.168.1.1
192.168.1.10
8.8.8.8
3) Run the Scanner:
sudo python3 port_scanner.py

License

This project is licensed under the MIT License

You are free to use, modify, and distribute it under the same license.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Contributing:

Pull requests are welcome! If you’d like to add more features (e.g., UDP scanning, multi-threading, banner grabbing), feel free to fork and improve this project.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
Disclaimer

This tool is for educational and authorized security testing only.
Do not use it on networks or systems you don’t own or have explicit permission to test.
-------------------------------------------------------------------------------------------------------------------------------------
