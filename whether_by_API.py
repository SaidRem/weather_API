import sys
import pprint
import requests
from dateutil.parser import parse


API_KEY_YAN_WEATHER = ''
API_KEY_YAN_GEO = ''


class YandexWeather:

    def get(self, city):
        url = f"https://api.weather.yandex.ru/v1/forecast?lat={geo[0]}&lon" \
            f"={geo[1]}&extra=true"
        headers = {'X-Yandex-API-Key': API_KEY_YAN_WEATHER}
        data = requests.get(url, headers=headers).json()
        forecast = {
            'temp': data['fact']['temp'],
            'pressure': data['fact']['pressure_mm']
        }
        return forecast


class CityInfo:
    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or YandexWeather()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def main(city):
    city_info = CityInfo(city)
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    city = input('Enter the city').strip()
    main(city)