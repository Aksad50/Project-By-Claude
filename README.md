# 🌦️ Weather App

A simple command-line weather app built with Python that shows real-time weather data for any city in the world.

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat&logo=python)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📸 Preview

```
🌦️  Welcome to Weather App!
   Type 'quit' to exit.

Enter city name: London

========================================
  📍 London, GB
========================================
  🌡️  Temperature  : 14°C
  🤔  Feels Like   : 12°C
  💧  Humidity     : 78%
  🌤️  Condition    : Overcast clouds
  💨  Wind Speed   : 4.5 m/s
========================================
```

---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Shows temperature, feels-like, humidity, wind speed & condition
- ❌ Handles errors gracefully (wrong city, no internet)
- 🔁 Loop mode — check multiple cities without restarting
- 🌍 Works for any city worldwide

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Get a free API key

1. Go to [openweathermap.org](https://openweathermap.org/)
2. Sign up for a **free account**
3. Navigate to **API Keys** in your dashboard
4. Copy your API key

### 4. Add your API key

Open `weather_app.py` and replace the placeholder:

```python
API_KEY = "your_api_key_here"   # 👈 Paste your key here
```

### 5. Run the app

```bash
python weather_app.py
```

---

## 🛠️ Built With

| Tool | Purpose |
|------|---------|
| [Python 3](https://www.python.org/) | Core language |
| [Requests](https://pypi.org/project/requests/) | HTTP API calls |
| [OpenWeatherMap API](https://openweathermap.org/api) | Weather data |

---

## 📁 Project Structure

```
weather-app/
│
├── weather_app.py   # Main application file
└── README.md        # Project documentation
```

---

## 🌐 API Reference

This project uses the [OpenWeatherMap Current Weather API](https://openweathermap.org/current).

- **Free tier**: 60 calls/minute, 1,000,000 calls/month
- **No credit card required**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome! Feel free to open an issue if you find a bug or have a feature suggestion.

---

> Made with ❤️ and Python
