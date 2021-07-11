import requests
import json
import os
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    #DB設定
    dynamodb = boto3.resource('dynamodb')
    TABLE = dynamodb.Table('atcoder_info')
    
    atcoder_id = event["atcoder_id"]
    
    #現在の情報のリクエスト
    url = 'https://kenkoooo.com/atcoder/atcoder-api/v2/user_info'
    headers = {"content-type": "application/json"}
    params = {'user': atcoder_id}
    
    response = requests.get(url, headers=headers, params=params)
    
    data = response.json()
    now_accepted_count = data["accepted_count"]
    now_new_ac = 0
    
    #DB書き込み
    table = dynamodb.Table('atcoder_info')
    table.put_item(
        Item={
            "atcoder_id": atcoder_id,
            "accepted_count": now_accepted_count,
            "new_ac": now_new_ac
       }
    )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
