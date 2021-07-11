import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def get_stalking_list(user_id):
    
    TABLE = dynamodb.Table(os.environ["STALKING_TABLE"])

    data = TABLE.query(
        KeyConditionExpression=Key('user_id').eq(user_id)
    )

    return data['Items']