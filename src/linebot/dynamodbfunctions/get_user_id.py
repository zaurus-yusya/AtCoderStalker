import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def get_user_id(line_user_id):
    TABLE = dynamodb.Table(os.environ["LINE_USER_TABLE"])

    data = TABLE.get_item(
        Key={
            'line_user_id': line_user_id
        }
    )

    return data['Item']['user_id']