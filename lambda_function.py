from typing import List
from DynamoDatabaseInterface import DynamoDatabaseInterface
from Processor import Processor
from GovWeatherAlertInterface import GovWeatherAlertInterface
from MultiMessageInterfaceWrapper import MultiMessageInterfaceWrapper
from SNSMessageInterface import SNSMessageInterface
from RequestsNetworkInterface import RequestsNetworkInterface
from ConsoleMessageInterface import ConsoleMessageInterface
from LoggerMessageInterface import LoggerMessageInterface
import os


def lambda_handler(event, context) -> None:

    # Set up configuration for which alerts to get
    states: List[str] = []  # ['NH', 'NY', 'MA', 'ME']
    zones: List[str] = ['NHC011']

    # Dependency injection
    Processor(
        weatherInterface=GovWeatherAlertInterface(
            RequestsNetworkInterface(), states, zones),
        messageInterface=MultiMessageInterfaceWrapper([
            ConsoleMessageInterface(),
            LoggerMessageInterface(filename='weather_alerts.txt'),
            SNSMessageInterface(
                topicArn=os.environ['topicArn'])
            ]
        ),
        databaseInterface=DynamoDatabaseInterface(tableName='weather')
    ).process()
