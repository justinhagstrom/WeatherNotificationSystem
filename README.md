# WeatherNotificationSystem

WeatherNotificationSystem is a Python application that sends text and/or email notifications based on warnings and alerts published by the National Weather Service's public API (https://www.weather.gov/alerts). WeatherNotificationSystem is designed to be run as an AWS Lambda function which can be triggered on a schedule by EventBridge.

WeatherNotificationSystem uses the following AWS services:
* ![Lambda](./icons/lambda.svg?raw=true) **Lambda** runs the python application using Lambda's python 3.8 environment
* ![EventBridge](./icons/eventbridge.svg?raw=true) **EventBridge** acts as a cron job to trigger the lambda on a set schedule
* ![DynamoDB](./icons/dynamodb.svg?raw=true) **DynamoDB** stores events that were already sent out to prevent duplicate messages
* ![SNS](./icons/sns.svg?raw=true) **SNS** is the notification service that sends out texts and emails 
* <img src="./icons/cloudformation.svg?raw=true" alt="CloudFormation" width="24"/> **CloudFormation** to represent the above infrastructure as code and to automate the provisioning of AWS services

## Installation

If running locally, use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies (boto3 and requests libraries).

```bash
pip3 install -r requirements.txt
```

If running on AWS Lambda, create a Layer using the requests.zip file (boto3 is included with Lambda by default, so only external dependency is the Requests library).

```bash
aws lambda publish-layer-version \
    --layer-name requests \
    --description "Requests library" \
    --content S3Bucket=lambda-layers-us-east-2-12345,S3Key=requests.zip \
    --compatible-runtimes python3.8
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)