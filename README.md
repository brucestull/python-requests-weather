# Python `requests` to Get Weather Forecast

- [Get 5-day Weather Forecast - ChatGPT - Private](https://chatgpt.com/c/68596128-1718-8002-bdc2-c5a42ae3d21a)

To get the weather forecast for the next 5 days using Python’s `requests` library, you can use a free weather API like [OpenWeatherMap](https://openweathermap.org/forecast5). Here's how to do it:

---

### ✅ Step-by-Step Instructions

#### 1. **Sign up for an API key**

* Go to: [https://openweathermap.org/api](https://openweathermap.org/api)
* Register and get a **free API key** for the **5-day/3-hour forecast** API.

---

#### 2. **Install `requests` (if not installed)**

```bash
pip install requests
```

---

#### 3. **Python Script Example**

```python
import requests

# Replace with your actual API key
API_KEY = 'your_openweathermap_api_key'
CITY = 'Columbus,US'  # Use "City,CountryCode"
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Send request
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    forecasts = data['list']
    print(f"Weather forecast for {CITY} (next 5 days):\n")

    # Print one forecast per day (at 12:00 noon)
    for forecast in forecasts:
        if '12:00:00' in forecast['dt_txt']:
            date = forecast['dt_txt'].split()[0]
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"{date}: {temp}°C, {description}")

else:
    print("Error:", data.get("message", "Failed to retrieve data"))
```

---

### 📝 Output Example

```
Weather forecast for Columbus,US (next 5 days):

2025-06-23: 26.5°C, broken clouds
2025-06-24: 28.1°C, light rain
2025-06-25: 29.0°C, clear sky
2025-06-26: 27.6°C, scattered clouds
2025-06-27: 25.8°C, moderate rain
```

---

Would you like a version that saves the forecast to a file or converts the temperatures to Fahrenheit?
