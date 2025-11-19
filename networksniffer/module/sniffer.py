from scapy.all import sniff

def process_packet(packet):
    print("="*60)
    print(f"[Time] {packet.time}")
    
    if packet.haslayer("IP"):
        print(f"[Source] {packet['IP'].src}")
        print(f"[Destination] {packet['IP'].dst}")
        print(f"[Protocol] {packet['IP'].proto}")

    if packet.haslayer("TCP"):
        print(f"[TCP] Src Port: {packet['TCP'].sport}, Dst Port: {packet['TCP'].dport}")

    if packet.haslayer("UDP"):
        print(f"[UDP] Src Port: {packet['UDP'].sport}, Dst Port: {packet['UDP'].dport}")

    if packet.haslayer("Raw"):
        print(f"[Data] {packet['Raw'].load[:50]}")
    print("="*60)


def start_sniffer(interface):
    sniff(iface=interface, prn=process_packet, store=False)
