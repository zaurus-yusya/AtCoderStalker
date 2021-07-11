import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def user_delete(line_user_id):
    TABLE = dynamodb.Table(os.environ["LINE_USER_TABLE"])

    TABLE.delete_item(
        Key={
            "line_user_id": line_user_id
        }
    )