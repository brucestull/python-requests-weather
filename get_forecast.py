import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual API key
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
CITY = os.getenv("CITY", "Columbus,US")  # Use "City,CountryCode"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    forecasts = data["list"]
    print(f"Weather forecast for {CITY} (next 5 days):\n")

    # Print one forecast per day (at 12:00 noon)
    for forecast in forecasts:
        if "12:00:00" in forecast["dt_txt"]:
            date = forecast["dt_txt"].split()[0]
            temp = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(f"{date}: {temp}°C, {description}")

else:
    print("Error:", data.get("message", "Failed to retrieve data"))
