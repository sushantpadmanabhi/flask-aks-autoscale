from flask import Flask
import time
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from AKS!"

@app.route('/load')
def load():
    def burn_cpu():
        end_time = time.time() + 15  # 15 seconds
        while time.time() < end_time:
            pass  # CPU loop

    thread = threading.Thread(target=burn_cpu)
    thread.start()
    return "CPU load started for 15 seconds!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
