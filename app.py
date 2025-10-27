from flask import Flask, render_template
import threading
from network_monitor import start_sniffing, packets_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', packets=packets_data)

def run_sniffer():
    start_sniffing()

if __name__ == '__main__':
    t = threading.Thread(target=run_sniffer, daemon=True)
    t.start()
    app.run(debug=True)

