from flask import Flask, jsonify
import socket
from datetime import datetime
import requests

app = Flask(__name__)

# Constants
VERSION = "1.0"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
WEATHER_PARAMS = {
    "latitude": 23.8103,  # Dhaka
    "longitude": 90.4125,
    "current_weather": True,
}


def get_weather():
    try:
        response = requests.get(WEATHER_API_URL, params=WEATHER_PARAMS, timeout=5)
        response.raise_for_status()
        data = response.json()
        temp = data["current_weather"]["temperature"]
        return {"temperature": str(temp), "temp_unit": "c"}
    except Exception as e:
        return {"temperature": "N/A", "temp_unit": "c", "error": str(e)}


@app.route("/api/hello", methods=["GET"])
def hello():
    weather = get_weather()
    return jsonify(
        {
            "hostname": socket.gethostname(),
            "datetime": datetime.now().strftime("%y%m%d%H%M"),
            "version": VERSION,
            "weather": {"dhaka": weather},
        }
    )


@app.route("/api/health", methods=["GET"])
def health():
    try:
        response = requests.get(WEATHER_API_URL, params=WEATHER_PARAMS, timeout=5)
        response.raise_for_status()
        return jsonify({"status": "ok", "weather_api": "reachable"}), 200
    except Exception as e:
        return (
            jsonify({"status": "error", "weather_api": "unreachable", "error": str(e)}),
            503,
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
