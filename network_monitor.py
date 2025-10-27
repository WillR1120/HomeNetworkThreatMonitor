from scapy.all import sniff
from datetime import datetime

packets_data = []

def packet_callback(packet):
    info = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "summary": packet.summary()
    }
    packets_data.append(info)
    # Keep only the latest 50 packets
    if len(packets_data) > 50:
        packets_data.pop(0)

def start_sniffing():
    sniff(prn=packet_callback, store=False)

