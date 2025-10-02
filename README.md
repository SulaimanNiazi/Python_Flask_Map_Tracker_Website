# Tracker Map

A simple Flask-based web app to track and visualize location updates on a map using Leaflet.js.

## Features

- Displays a map centered on the server's location (via IP geolocation).
- Allows real-time updates of location and label via a REST API.
- Shows a marker and popup label for the current location.
- Draws a trail as the location changes.

## Folder Structure

- `src/main.py` — Flask server, serves the map and API endpoints.
- `src/update.py` — Script to send location updates to the server.
- `templates/index.html` — HTML template for the map UI.
- `requirements.txt` — Python dependencies.

## Getting Started

### 1. Install dependencies

```sh
pip install -r requirements.txt
```

### 2. Run the server

```sh
python src\main.py
```

The app will start at [http://127.0.0.1:5000](http://127.0.0.1:5000) or some other port mentioned in terminal output of [main.py](src/main.py).

### 3. Send location updates

You can update the location using the provided script:

```sh
python src\update.py
```

Or call `update(lat, lon, label)` from [update.py](src/update.py) with your desired coordinates.

## API Endpoints

- `GET /` — Map UI.
- `GET /location` — Current location as JSON.
- `POST /add` — Update location. JSON body: `{ "lat": float, "lon": float, "label": str }`

## License

MIT License