from typing import Dict
from NetworkInterface import NetworkInterface


class GovWeatherForecastInterface:
    class Gridpoint:
        def __init__(self, station, gridpoint) -> None:
            self.station = station
            self.gridpoint = gridpoint

        def __str__(self) -> str:
            return f"self.station/self.gridpoint"

    def __init__(self, networkInterface: NetworkInterface, gridpoints) -> None:
        self.networkInterface = networkInterface
        self.gridpoints = gridpoints

    def __apiCall(self, url: str) -> Dict:
        r = self.networkInterface.get(url)
        if 'properties' in r:
            return r['properties']
        return {}

    def getRawData(self, gridpoint) -> Dict:
        return self.__apiCall(f'https://api.weather.gov/gridpoints/{str(gridpoint)}')

    def getForecast(self, gridpoint) -> Dict:
        return self.__apiCall(f'https://api.weather.gov/gridpoints/{str(gridpoint)}/forecast')

    def getHourlyForecast(self, gridpoint) -> Dict:
        return self.__apiCall(f'https://api.weather.gov/gridpoints/{str(gridpoint)}/forecast/hourly')
