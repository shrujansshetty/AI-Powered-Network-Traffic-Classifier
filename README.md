# AI Network Traffic Classifier (short)

What it does:

- Capture network packet/flow data
- Train a machine-learning model from extracted features
- Classify live traffic using the trained model

Run Intructions (Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy scikit-learn joblib scapy
```

- Capture network packets:

```bash
sudo python3 capture_packets.py
```

- Train model :

```bash
sudo python3 train_model.py
```

- Run live classifier:

```bash
sudo python3 classify_live.py
```

