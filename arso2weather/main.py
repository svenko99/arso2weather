import requests
import xml.etree.ElementTree as ET

# URL of website to scrape data
url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml"
response = requests.get(url)
error_msg = "ARSO weather is currently not working"
root = ET.fromstring(response.content)


class Arso2Weather:
    def __init__(self, city=None) -> None:
        self.city = city

    # Function weather takes two inputs:
    # city, round_temp
    # city (The city you want to get temperature), round_temp (False to not round temperature) <- (OPTIONAL)
    def weather_temp(self, round_temp=True):
        for city_in in root.findall("metData"):
            if self.city.upper() == city_in.find("domain_longTitle").text.upper():
                temperature = float(city_in.find("t").text)
                return round(temperature) if round_temp else temperature
        return "Please enter valid city i.e. Ljubljana"

    # Function all_weather outputs temperature of all available cities in dictionary
    # It takes one optional parameter to display temperature ronded or not rounded
    def all_weather_temp(self, round_temp=True):
        all_cites = {}
        try:
            for city_in in root.findall("metData"):
                temperature = float(city_in.find("t").text)
                all_cites[city_in.find("domain_longTitle").text] = (
                    round(temperature) if round_temp else temperature
                )
            return all_cites if len(all_cites) else error_msg
        except TypeError:
            return error_msg

    def sunrise(self):
        for city_in in root.findall("metData"):
            if self.city.upper() == city_in.find("domain_longTitle").text.upper():
                return city_in.find("sunrise").text

    def sunset(self):
        for city_in in root.findall("metData"):
            if self.city.upper() == city_in.find("domain_longTitle").text.upper():
                return city_in.find("sunset").text
