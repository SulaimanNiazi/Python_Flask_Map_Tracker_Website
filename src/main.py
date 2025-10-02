from flask import Flask, jsonify, render_template, request
import geocoder

app = Flask(__name__)

# start with some seed point
lat, lon, label = None, None, None

def get_location():
    try:
        g = geocoder.ip('me')
        lat, lon = g.latlng
        return lat, lon, "Server Location (Tracker not detected yet)"
    except Exception as e:
        print("Error:", e)
        return 0, 0, "No Data"

@app.route("/")
def index():
    global lat, lon, label
    if lat is None or lon is None:
        lat, lon, label = get_location()
    
    return render_template("index.html", lat=lat, lon=lon, label=label)

@app.route("/location")
def location():
    return jsonify({"lat": lat, "lon": lon, "label": label})

# optional: an API endpoint to add new points
@app.route("/add", methods=["POST"])
def add():
    global lat, lon, label
    data = request.get_json(force=True)
    lat, lon = float(data["lat"]), float(data["lon"])
    label = data.get("label", "Tracker")
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
