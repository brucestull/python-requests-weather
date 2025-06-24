# process_weather.py
from collections import defaultdict, Counter

def summarize_daily_weather(data):
    grouped = defaultdict(list)
    for entry in data["list"]:
        date = entry["dt_txt"].split()[0]
        description = entry["weather"][0]["description"]
        grouped[date].append(description)

    # Pick most common weather description per day
    return {
        date: Counter(descriptions).most_common(1)[0][0]
        for date, descriptions in grouped.items()
    }
