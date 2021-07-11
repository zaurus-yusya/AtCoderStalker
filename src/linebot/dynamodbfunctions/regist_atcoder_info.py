import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

import requests
import json

def regist_atcoder_info(atcoder_id):
    #AC数の取得
    res = requests.get('https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user=' + atcoder_id)
    accepted_count = res.json()['count']

    #RPSの取得
    res = requests.get('https://kenkoooo.com/atcoder/resources/sums.json')
    data = res.json()
    rated_point_sum = -1
    for item in data:
        if item['user_id'] == atcoder_id:
            rated_point_sum = int(item['point_sum'])
            break
    if rated_point_sum == -1:
        #何らかの事情でrpsが取得できなかったら終了
        return

    #DBに登録
    TABLE = dynamodb.Table(os.environ["ATCODER_INFO_TABLE"])

    data = TABLE.put_item(
        Item={
            'atcoder_id': atcoder_id,
            'accepted_count': accepted_count,
            'new_ac': 0,
            'rated_point_sum': rated_point_sum
        }
    )