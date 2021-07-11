import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def get_last_sent_time():
    #前回push messageを送った時刻を取得
    TABLE = dynamodb.Table(os.environ["PUSH_TIME_TABLE"])
    
    response = TABLE.get_item(
        Key={
            'unique_flag': 0
        }
    )

    item = response['Item']['time_sent']
    last_sent_time = item[5:] # 2020/06/07 01:19 → 06/07 01:19

    return last_sent_time