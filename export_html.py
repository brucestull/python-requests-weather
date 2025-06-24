# export_html.py
def export_html(filename, city, country, summary):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"<title>Weather Forecast: {city}, {country}</title>")
        f.write(f"<h1>��️ Weather Forecast for {city}, {country}</h1>\n")
        f.write("<table border='1' cellspacing='0' cellpadding='4'>\n")
        f.write(
            "<tr><th>Date</th><th>Temp (°C)</th><th>Feels Like (°C)</th><th>Description</th><th>Icon</th></tr>\n"  # noqa: E501
        )
        for entry in summary:
            f.write(
                f"<tr><td>{entry['date']}</td><td>{entry['temp']}</td>"
                f"<td>{entry['feels_like']}</td><td>{entry['description']}</td>"  # noqa: E501
                f"<td><img src='{entry['icon_url']}'></td></tr>\n"
            )
        f.write("</table>")
