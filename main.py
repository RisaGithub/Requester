import flet as ft
import requests
import time

# List of URLs to send GET requests to
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


def main(page: ft.Page):
    while True:
        send_get_requests()
        print("Waiting for 10 minutes...")
        time.sleep(600)  # Wait for 10 minutes (600 seconds)


ft.app(target=main)
