from scapy.all import IP, TCP, UDP, ICMP, ARP, Raw
from datetime import datetime

def analyze_packet(packet):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n==============================")
    print(f"Time: {time}")

    # IP packets
    if packet.haslayer(IP):
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")

        # TCP
        if packet.haslayer(TCP):
            print(f"Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        # UDP
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        # ICMP (ping)
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP (Ping)")

    # ARP packets
    elif packet.haslayer(ARP):
        print("Protocol: ARP")
        print(f"ARP Source: {packet[ARP].psrc}")
        print(f"ARP Destination: {packet[ARP].pdst}")

    # Payload
    if packet.haslayer(Raw):
        data = packet[Raw].load
        try:
            print("Payload:", data.decode(errors="ignore"))
        except:
            print("Payload: [Binary data]")

    print("==============================")
