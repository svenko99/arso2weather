# ☁️ Arso2weather

### 🤔 What is it?

- Arso2weather is a small package that allows you to look up the current temperature of most Slovenian cities

- It can also output sunrise/sunset of Slovenian cities

- Temperature is displayed in Celsius (C°)

- The package is using [ARSO Vreme](https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml) data


### Installation

```
pip3 install arso2weather
```

### Usage

```
from arso2weather import Arso2Weather

city = Arso2Weather("Ljubljana")
temp = city.weather_temp()
sunrise = city.sunrise()
sunset = city.sunset()
all_cities_temp = Arso2Weather().all_weather_temp()

print(temp, sunrise, sunset)
print(all_cities_temp)
```
