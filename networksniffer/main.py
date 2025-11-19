from module.sniffer import start_sniffer

def main():
    print("=== Network Packet Sniffer ===")
    print("Example interfaces: eth0, wlan0, Wi-Fi, Ethernet")

    interface = input("Enter your network interface: ").strip()

    print(f"\n[+] Starting packet capture on: {interface}")
    print("[+] Showing packets like Wireshark...\n")

    start_sniffer(interface)

if __name__ == "__main__":
    main()
