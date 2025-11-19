# 🛰️ NetMonitor – Python Network Packet Sniffer

NetMonitor is a lightweight, Wireshark-style packet sniffer built using Python and Scapy.
It captures live network packets, analyzes protocols, and displays clean readable output for learning, security testing, and traffic monitoring.

# 📌 Features

✔ Real-time packet capturing

✔ Shows Source IP, Destination IP, Protocol, Ports

✔ Clean readable output (no messy symbols)

✔ Works on Windows (with Npcap) and Kali Linux

✔ CLI-based, easy to understand

✔ Perfect for cybersecurity students & pentesters

# 📥 Installation
🔹 1. Install Python

Download from: https://www.python.org/downloads/

Make sure you check:
✔ Add to PATH

🪟 Windows Installation (VS Code)
Step 1 — Install Npcap (Required)

Download Npcap:
https://npcap.com/#download

Install with:

✔ Support raw 802.11 traffic

✔ WinPcap API compatibility

Step 2 — Install Scapy
pip install scapy

Step 3 — Open project in VS Code
cd NetMonitor
code .

Step 4 — Run the tool
python main.py

# 🐉 Kali Linux Installation

Scapy is already included, but update it:

sudo apt update
sudo apt install python3-pip
pip install scapy --break-system-packages


Run with root:

sudo python3 main.py

# 🚀 Usage
When the program starts:

It will show something like:

=== Network Packet Sniffer ===

Available Interfaces (Windows examples):
 - Wi-Fi
 - Ethernet
 - VMware Network Adapter VMnet1

Enter your network interface name exactly:


👉 Windows Example

Wi-Fi


👉 Kali Linux Example

wlan0
eth0

Example Output
[+] Packet Captured
Source: 192.168.1.10 → Destination: 8.8.8.8
Protocol: TCP | Sport: 53212 | Dport: 80

# ⚙️ How It Works

NetMonitor uses Scapy, a powerful packet manipulation library.
It listens on a selected network interface and captures packets in real time.

The tool:

Reads raw packets

Identifies protocol (TCP, UDP, ICMP, ARP…)

Extracts header information

Prints clean results like Wireshark (terminal version)

# 📁 Folder Structure
NetMonitor/
│
├── main.py
└── module/
    └── sniffer.py

# 🧑‍💻 Run as Administrator

Windows sniffing needs admin rights:

Run VS Code as Administrator

Or run terminal as Administrator

# 🛡 Disclaimer

This tool is for learning and ethical testing only.
Do not capture packets on networks without permission.
