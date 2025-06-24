# process_temperature.py
from collections import defaultdict
from statistics import mean

def group_daily_values(data, key):
    grouped = defaultdict(list)
    for entry in data["list"]:
        date = entry["dt_txt"].split()[0]
        grouped[date].append(entry["main"][key])
    return {date: round(mean(values), 2) for date, values in grouped.items()}

def summarize_daily_temps(data):
    avg_temp = group_daily_values(data, "temp")
    avg_feels_like = group_daily_values(data, "feels_like")
    return {
        date: {"avg_temp": avg_temp[date], "avg_feels_like": avg_feels_like[date]}
        for date in avg_temp
    }
