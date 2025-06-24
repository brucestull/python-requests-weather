# export_markdown.py
def export_markdown(filename, city, country, summary):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 🌤️ Weather Forecast for {city}, {country}\n\n")
        f.write("| Date       | Temp (°C) | Feels Like (°C) | Description     | Icon |\n")
        f.write("|------------|-----------|------------------|------------------|------|\n")
        for entry in summary:
            f.write(
                f"| {entry['date']} | {entry['temp']} | {entry['feels_like']} "
                f"| {entry['description']} | ![]({entry['icon_url']}) |\n"
            )
