from typing import Iterable
from MessageInterface import MessageInterface


class MultiMessageInterfaceWrapper:
    def __init__(self, messageInterfaces: Iterable[MessageInterface]) -> None:
        self.messageInterfaces: Iterable[MessageInterface] = messageInterfaces

    def sendMessage(self, messageStr: str) -> bool:
        return True in [i.sendMessage(messageStr) for i in self.messageInterfaces]
