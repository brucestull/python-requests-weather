# main.py
from load_forecast import load_forecast
from process_temperature import summarize_daily_temps
from process_weather import summarize_daily_weather

filename = "forecast_columbus_us_20250624_154343.json"
data = load_forecast(filename)

temps = summarize_daily_temps(data)
weather = summarize_daily_weather(data)


def get_icon_code_for_date(data, target_date):
    """Returns the icon code for the 12:00:00 entry if available, else the first match of the day."""  # noqa E501
    for entry in data["list"]:
        dt_txt = entry["dt_txt"]
        if dt_txt.startswith(target_date):
            if "12:00:00" in dt_txt:
                return entry["weather"][0]["icon"]
    # fallback: return first matching date's icon
    for entry in data["list"]:
        if entry["dt_txt"].startswith(target_date):
            return entry["weather"][0]["icon"]
    return "unknown"


print(
    f"\n📍 Forecast Summary for {data['city']['name']}, {data['city']['country']}:\n"  # noqa E501
)  # noqa E501

for date in sorted(temps.keys()):
    temp = temps[date]["avg_temp"]
    feels = temps[date]["avg_feels_like"]
    desc = weather.get(date, "n/a")
    icon_code = get_icon_code_for_date(data, date)
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    print(f"{date}: {temp}°C (feels like {feels}°C), {desc} — {icon_url}")
