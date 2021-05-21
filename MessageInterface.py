from typing import Protocol


class MessageInterface(Protocol):
    def sendMessage(self, messageStr: str) -> bool: ...
