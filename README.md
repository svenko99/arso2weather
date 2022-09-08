# Arso2weather

### What is it?

- Arso2weather is a small package that allows you to look up the current temperature of specific Slovenian cities.

- Temperature is displayed in Celsius (C°).

- The package is using [ARSO Vreme](https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml) data.

### Installation

```
pip3 install arso2weather
```

### Usage

```
import arso2weather as arso

city_temperature = arso.weather_temp("Ljubljana")
city2_temperature = arso.weather_temp("Logatec", round_temp=False)
all_cites_temperature = arso.all_weather_temp()

print(city_temperature)
print(all_cites_temperature)
print(all_cites_temperature["Maribor"])

```
