from scapy.all import sniff, IP, TCP, UDP
import joblib
import numpy as np

model = joblib.load("traffic_model.pkl")
scaler = joblib.load("scaler.pkl")

def classify(pkt):
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

        features = np.array([[proto, sport, dport, length, ttl]])
        scaled = scaler.transform(features)
        prediction = model.predict(scaled)[0]

        labels = {0: "HTTP", 1: "FTP", 2: "VoIP"}
        print(f"Predicted Traffic: {labels.get(prediction, 'Unknown')}")

sniff(count=20, prn=classify)
