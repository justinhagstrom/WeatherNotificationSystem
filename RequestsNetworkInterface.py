from typing import Any
import requests
import time


class RequestsNetworkInterface:
    def __init__(self) -> None:
        self.madeFirstCall: bool = False

    def get(self, url: str) -> Any:
        if self.madeFirstCall:
            time.sleep(1)
        else:
            self.madeFirstCall = True
        return requests.get(url).json()
