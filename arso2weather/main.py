import requests
import xml.etree.ElementTree as ET

# URL of website to scrape data
url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_si_latest.xml"
response = requests.get(url)
error_msg = "ARSO weather is currently not working"
root = ET.fromstring(response.content).findall("metData")


class Arso2Weather:
    def __init__(self, city=None) -> None:

        self.city = city

        equals_city = [
            city_in
            for city_in in root
            if self.city.upper() == city_in.find("domain_longTitle").text.upper()
        ]

        word_in_city = [
            city_in
            for city_in in root
            if self.city.upper() in city_in.find("domain_longTitle").text.upper()
            and len(self.city) > 3
            # last line in list avoids that random inputs like ("pt") are not outputed
        ]

        # It returns equals_city if input equals "domain_longTitle" else word_in_cit    y
        # I did this because some "domain_longTitle" of cites are not exactly like city i.e "Koper" city has "Luka-Koper" domain_longTitle
        self.xml_of_city = equals_city or word_in_city

    # round_temp (False to not round temperature) <- (OPTIONAL)
    def weather_temp(self, round_temp=True):
        for i in self.xml_of_city:
            temperature = float(i.find("t").text)
            return round(temperature) if round_temp else temperature

    # Function all_weather outputs temperature of all available cities in dictionary
    # It takes one optional parameter to display temperature rounded or not rounded
    def all_weather_temp(self, round_temp=True):
        all_cites = {}
        try:
            for city_in in root:
                temperature = float(city_in.find("t").text)
                all_cites[city_in.find("domain_longTitle").text] = (
                    round(temperature) if round_temp else temperature
                )
            return all_cites if len(all_cites) else error_msg
        except TypeError:
            return error_msg

    def sunrise(self):
        return [rise.find("sunrise").text for rise in self.xml_of_city][0]

    def sunset(self):
        return [rise.find("sunset").text for rise in self.xml_of_city][0]

    # useful if you woud like to get icon url -> f"https://meteo.arso.gov.si/uploads/meteo/style/img/weather/{Arso2Weather.icon()}.png"
    # fmt: off
    def icon(self):
        return [rise.find("nn_icon-wwsyn_icon").text for rise in self.xml_of_city][0] or "error"
