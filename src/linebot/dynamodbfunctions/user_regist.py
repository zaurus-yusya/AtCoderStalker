import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def user_regist(line_user_id, user_id):
    TABLE = dynamodb.Table(os.environ["LINE_USER_TABLE"])

    TABLE.put_item(
        Item={
            "line_user_id": line_user_id,
            "user_id": user_id
        }
    )