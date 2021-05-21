from typing import Protocol, Any


class NetworkInterface(Protocol):
    def get(self, url: str) -> Any: ...
