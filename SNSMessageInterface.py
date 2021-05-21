import boto3  # type: ignore


class SNSMessageInterface:
    def __init__(self, topicArn: str) -> None:
        self.sns = boto3.client('sns')
        self.sns.set_sms_attributes(attributes={
            'DefaultSMSType': 'Transactional'
        })
        self.topicArn: str = topicArn

    def sendMessage(self, messageStr: str) -> bool:
        response = self.sns.publish(TopicArn=self.topicArn, Message=messageStr)
        id = response['MessageId'] if 'MessageId' in response else ''
        print(f"MessageId: {id}")
        return id != ''
