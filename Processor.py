from typing import Optional, Tuple, List
from MessageInterface import MessageInterface


class Processor:
    def __init__(self, weatherInterface, messageInterface: MessageInterface, databaseInterface=None):
        self.weatherInterface = weatherInterface
        self.messageInterface = messageInterface
        self.databaseInterface = databaseInterface

    def __processEvent(self, id: str, message: str) -> Optional[Tuple[str, str]]:
        if self.databaseInterface:
            if not self.databaseInterface.isInDB(id) and self.messageInterface.sendMessage(message):
                self.databaseInterface.addToDB(id)
                return id, message
        elif self.messageInterface.sendMessage(message):
            return id, message
        return None

    def process(self) -> List[Optional[Tuple[str, str]]]:
        return [self.__processEvent(id=key, message=value) for key, value in self.weatherInterface.getEvents().items() if key and value]
