from scapy.all import sniff, IP, TCP, UDP
import pandas as pd

data = []

def extract_features(pkt):
    if IP in pkt:
        ip = pkt[IP]
        proto = ip.proto
        length = len(pkt)
        ttl = ip.ttl
        sport = dport = 0

        if TCP in pkt:
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
        elif UDP in pkt:
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport

        data.append([proto, sport, dport, length, ttl])

sniff(count=200, prn=extract_features)
df = pd.DataFrame(data, columns=["protocol", "sport", "dport", "length", "ttl"])

# Label manually for training depending on what to capture(e.g., HTTP=0, FTP=1, VOIP=2)
df["label"] = 0 
df.to_csv("traffic_data.csv", index=False)
print("Captured and saved packet data to traffic_data.csv")
