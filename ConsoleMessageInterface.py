class ConsoleMessageInterface:
    def __init__(self):
        pass

    def sendMessage(self, messageStr: str) -> bool:
        print('---------- NEW ALERT ----------')
        print(messageStr)
        return True
