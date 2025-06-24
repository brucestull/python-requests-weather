# main.py
from load_forecast import load_forecast
from process_temperature import summarize_daily_temps
from process_weather import summarize_daily_weather

filename = "forecast_columbus_us_20250624_154343.json"
data = load_forecast(filename)

temps = summarize_daily_temps(data)
weather = summarize_daily_weather(data)

print(f"\n📍 Forecast Summary for {data['city']['name']}, {data['city']['country']}:\n")

for date in sorted(temps.keys()):
    temp = temps[date]["avg_temp"]
    feels = temps[date]["avg_feels_like"]
    desc = weather.get(date, "n/a")
    print(f"{date}: {temp}°C (feels like {feels}°C), {desc}")
