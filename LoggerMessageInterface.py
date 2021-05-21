import logging


class LoggerMessageInterface:
    def __init__(self, filename: str) -> None:
        self.logger = logging.getLogger(filename)

    def sendMessage(self, messageStr: str) -> bool:
        self.logger.info(messageStr)
        return True
