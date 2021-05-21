from GovWeatherAlertInterface import GovWeatherAlertInterface
from Processor import Processor


class MockNetworkInterface:
    def __init__(self):
        self.counter = 122

    # IDs will start at 123 and then increment each time
    def get(self, url):
        self.counter += 1
        return {"features": [{"id": self.counter, "properties": {"headline": "testHeadline", "description": "testDescription", "instruction": "testInstruction"}}]}


class MockMessageInterface:
    def __init__(self):
        pass

    def sendMessage(self, str):
        return True


class MockDatabaseInterface:
    def __init__(self, mockInDBResult):
        self.mockInDBResult = mockInDBResult

    def isInDB(self, id):
        return self.mockInDBResult

    def addToDB(self, id):
        pass


events = GovWeatherAlertInterface(
    MockNetworkInterface(), ['test'], ['test']).getEvents()
assert len(events) == 2
assert events[123] == "testHeadline\ntestDescription\ntestInstruction\n"
assert events[124] == "testHeadline\ntestDescription\ntestInstruction\n"

results = Processor(
    weatherInterface=GovWeatherAlertInterface(
        MockNetworkInterface(), ['test'], ['test']),
    messageInterface=MockMessageInterface(),
    databaseInterface=None).process()
assert len(results) == 2
assert results[0] == (123, "testHeadline\ntestDescription\ntestInstruction\n")
assert results[1] == (124, "testHeadline\ntestDescription\ntestInstruction\n")

results = Processor(
    weatherInterface=GovWeatherAlertInterface(
        MockNetworkInterface(), ['test'], ['test']),
    messageInterface=MockMessageInterface(),
    databaseInterface=MockDatabaseInterface(False)).process()
assert len(results) == 2
assert results[0] == (123, "testHeadline\ntestDescription\ntestInstruction\n")
assert results[1] == (124, "testHeadline\ntestDescription\ntestInstruction\n")

results = Processor(
    weatherInterface=GovWeatherAlertInterface(
        MockNetworkInterface(), ['test'], ['test']),
    messageInterface=MockMessageInterface(),
    databaseInterface=MockDatabaseInterface(True)).process()
assert len(results) == 2
assert results[0] == None
assert results[1] == None
