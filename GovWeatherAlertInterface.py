from typing import List, Dict
from NetworkInterface import NetworkInterface


class GovWeatherAlertInterface:
    def __init__(self, networkInterface: NetworkInterface, states: List[str], zones: List[str]) -> None:
        self.networkInterface = networkInterface
        self.states: List[str] = states
        self.zones: List[str] = zones

    def __constructMessage(self, headline: str, desc: str, instruction: str) -> str:
        result: str = ''
        if headline != None:
            result += headline + "\n"
        if desc != None:
            result += desc + "\n"
        if instruction != None:
            result += instruction + "\n"
        return result

    def __apiCall(self, url: str) -> Dict:
        results: Dict = {}
        r = self.networkInterface.get(url)
        if 'features' in r:
            for feature in r['features']:
                if 'properties' in feature and 'id' in feature:
                    properties = feature['properties']
                    message: str = self.__constructMessage(
                        properties['headline'], properties['description'], properties['instruction'])
                    if message:
                        results[feature['id']] = message
        return results

    def __processState(self, state: str) -> Dict:
        return self.__apiCall('https://api.weather.gov/alerts/active?area='+state)

    def __processStates(self) -> Dict:
        return {k: v for d in [self.__processState(state) for state in self.states] for k, v in d.items()}

    def __processZone(self, zone: str) -> Dict:
        return self.__apiCall('https://api.weather.gov/alerts/active/zone/'+zone)

    def __processZones(self) -> Dict:
        return {k: v for d in [self.__processZone(zone) for zone in self.zones] for k, v in d.items()}

    def getEvents(self) -> Dict:
        # requires python 3.5+
        return {**self.__processStates(), **self.__processZones()}
        # return self.__processStates() | self.__processZones() #requires python 3.9+
