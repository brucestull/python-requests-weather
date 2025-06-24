# main.py
from load_forecast import load_forecast
from process_temperature import summarize_daily_temps
from process_weather import summarize_daily_weather
from export_markdown import export_markdown
from export_html import export_html

HTML_FILENAME = "forecast_summary.html"
MARKDOWN_FILENAME = "forecast_summary.md"

filename = "forecast_columbus_us_20250624_154343.json"
data = load_forecast(filename)

temps = summarize_daily_temps(data)
weather = summarize_daily_weather(data)


def get_icon_code_for_date(data, target_date):
    for entry in data["list"]:
        if (
            entry["dt_txt"].startswith(target_date)
            and "12:00:00" in entry["dt_txt"]  # noqa: E501
        ):  # noqa: E501
            return entry["weather"][0]["icon"]
    for entry in data["list"]:
        if entry["dt_txt"].startswith(target_date):
            return entry["weather"][0]["icon"]
    return "unknown"


# Build summary
summary = []
for date in sorted(temps.keys()):
    icon = get_icon_code_for_date(data, date)
    summary.append(
        {
            "date": date,
            "temp": temps[date]["avg_temp"],
            "feels_like": temps[date]["avg_feels_like"],
            "description": weather.get(date, "n/a"),
            "icon_url": f"https://openweathermap.org/img/wn/{icon}@2x.png",
        }
    )

# Print
city = data["city"]["name"]
country = data["city"]["country"]
print(f"\n📍 Forecast Summary for {city}, {country}:\n")
for entry in summary:
    print(
        f"{entry['date']}: {entry['temp']}°C (feels like {entry['feels_like']}°C), {entry['description']} — {entry['icon_url']}"  # noqa: E501
    )

# Export
export_markdown(MARKDOWN_FILENAME, city, country, summary)
export_html(HTML_FILENAME, city, country, summary)
print(f"\n✅ Exported to '{HTML_FILENAME}' and '{MARKDOWN_FILENAME}'.\n")
