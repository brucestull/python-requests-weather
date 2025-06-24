# get_forecast.py
import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime
import re

load_dotenv()

# Load API key and city
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
CITY = os.getenv("CITY", "Columbus,US")  # Use "City,CountryCode"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"  # noqa: E501


# Slugify city name (e.g., Columbus,US -> columbus_us)
def slugify_city(city):
    return re.sub(r"[^a-z0-9]+", "_", city.lower())


# Generate timestamped filename
def forecast_filename(city):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"forecast_{slugify_city(city)}_{timestamp}.json"


# Send request
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    # Save the full data to file
    filename = forecast_filename(CITY)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n✅ Full forecast data saved to '{filename}'")

    # Print summary forecast
    forecasts = data["list"]
    print(f"\nWeather forecast for {CITY} (next 5 days):\n")
    for forecast in forecasts:
        if "12:00:00" in forecast["dt_txt"]:
            date = forecast["dt_txt"].split()[0]
            temp = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(f"{date}: {temp}°C, {description}")

else:
    print("❌ Error:", data.get("message", "Failed to retrieve data"))
