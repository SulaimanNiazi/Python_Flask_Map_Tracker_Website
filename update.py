import requests
import time

port = 5000 # Ensure this matches the server port from terminal output of main.py

def update(lat = 0, lon = 0, label = "Tracker"):
    time.sleep(5)
    url = f"http://127.0.0.1:{port}/add"
    payload = {
        "lat": lat,
        "lon": lon,
        "label": label
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # raise exception if not 2xx
        print("✅ Success:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    update(34, 73, "New Location")