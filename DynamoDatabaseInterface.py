import boto3  # type: ignore


class DynamoDatabaseInterface:
    def __init__(self, tableName: str):
        self.db = boto3.client('dynamodb')
        self.tableName: str = tableName

    def isInDB(self, id: str) -> bool:
        response = self.db.get_item(
            TableName=self.tableName, Key={'id': {"S": id}})
        return 'Item' in response

    def addToDB(self, id: str) -> None:
        self.db.put_item(TableName=self.tableName, Item={'id': {"S": id}})
