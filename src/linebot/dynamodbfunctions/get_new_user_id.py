import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def get_new_user_id(table_name):
    TABLE = dynamodb.Table(os.environ["SEQUENCE_TABLE"])

    data = TABLE.get_item(
        Key={
            'name': table_name
        }
    )

    current_number = data['Item']['current_number']

    TABLE.put_item(
        Item={
            "name": table_name,
            "current_number": current_number + 1
        }
    )

    return current_number + 1