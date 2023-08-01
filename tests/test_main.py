import unittest
from arso2weather.main import Arso2Weather

class TestArso2Weather(unittest.TestCase):
    def test_weather_temp(self):
        arso = Arso2Weather(city="Ljubljana")
        self.assertIsInstance(arso.weather_temp(), float)

    def test_all_weather_temp(self):
        arso = Arso2Weather()
        self.assertIsInstance(arso.all_weather_temp(), dict)

    def test_sunrise(self):
        arso = Arso2Weather(city="Ljubljana")
        self.assertIsInstance(arso.sunrise(), str)

    def test_sunset(self):
        arso = Arso2Weather(city="Ljubljana")
        self.assertIsInstance(arso.sunset(), str)

    def test_icon(self):
        arso = Arso2Weather(city="Ljubljana")
        self.assertIsInstance(arso.icon(), str)

if __name__ == '__main__':
    unittest.main()