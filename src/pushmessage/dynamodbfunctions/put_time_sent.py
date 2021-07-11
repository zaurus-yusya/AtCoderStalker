import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def put_time_sent(now_datetime_string):
    TABLE = dynamodb.Table(os.environ["PUSH_TIME_TABLE"])

    TABLE.put_item(
        Item={
            "unique_flag": 0,
            "time_sent": now_datetime_string
        }
    )