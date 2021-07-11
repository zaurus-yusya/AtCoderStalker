import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def is_already_stalking(user_id, atcoder_id):
    
    TABLE = dynamodb.Table(os.environ["STALKING_TABLE"])

    data = TABLE.query(
        KeyConditionExpression=Key('user_id').eq(user_id) & Key('atcoder_id').eq(atcoder_id)
    )

    if(data['Count'] == 1):
        return True
    else:
        return False