import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def regist_stalking_list(user_id, atcoder_id):
    TABLE = dynamodb.Table(os.environ["STALKING_TABLE"])

    data = TABLE.put_item(
        Item={
            'user_id': user_id,
            'atcoder_id': atcoder_id
        }
    )