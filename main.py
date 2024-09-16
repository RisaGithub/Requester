import requests
import time
from flask import Flask

app = Flask(__name__)

urls = [
    "https://contentmaster.onrender.com",
    "https://g4f-api-u0fr.onrender.com",
]

def send_get_requests():
    for url in urls:
        try:
            print(f"SEND GET request to {url}")
            response = requests.get(url)
            print(
                f"FINISHED GET request to {url} returned status code: {response.status_code}"
            )
        except requests.exceptions.RequestException as e:
            print(f"Error requesting {url}: {e}")

@app.route('/')
def index():
    return "Background task running."

if __name__ == "__main__":
    while True:
        send_get_requests()
        time.sleep(600)  # Wait for 10 minutes
        # Flask app binding to port
    app.run(host='0.0.0.0', port=5000)
