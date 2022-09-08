import requests
import xml.etree.ElementTree as ET


# URL of website to scrape data
url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml"
r = requests.get(url)
error_msg = "ARSO weather is currently not working"

# root of xml data
root = ET.fromstring(r.content)


# Function weather takes two inputs: city (The city you want to get temperature),
#                                    round_temp (False to not round temperature) <- (OPTIONAL)
def weather_temp(city=None, round_temp=True):
    try:
        for city_in in root.findall("metData"):
            if city.upper() == city_in.find("domain_longTitle").text.upper():
                temperature = float(city_in.find("t").text)
                return round(temperature) if round_temp else temperature
    except AttributeError:
        return "Please enter valid city i.e. Ljubljana"


# Function all_weather outputs temperature of all available cities in dictionary
# It takes one optional parameter to display temperature ronded or not rounded
def all_weather_temp(round_temp=True):
    all_cites = {}
    try:
        for city_in in root.findall("metData"):
            temperature = float(city_in.find("t").text)
            all_cites[city_in.find("domain_longTitle").text] = (
                round(temperature) if round_temp else temperature
            )
        return all_cites if len(all_cites) else error_msg
    except Exception:
        return error_msg
