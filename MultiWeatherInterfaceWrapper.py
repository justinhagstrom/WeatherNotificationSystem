from typing import Dict, Iterable


class MultiWeatherInterfaceWrapper:
    def __init__(self, weatherInterfaces: Iterable) -> None:
        self.weatherInterfaces: Iterable = weatherInterfaces

    def getEvents(self) -> Dict:
        results = {}
        for i in self.weatherInterfaces:
            results.update(i.getEvents())
        return results
