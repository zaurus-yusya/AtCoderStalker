import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def is_first_time_regist_atcoder_id(atcoder_id):
    
    TABLE = dynamodb.Table(os.environ["ATCODER_INFO_TABLE"])

    data = TABLE.query(
        KeyConditionExpression=Key('atcoder_id').eq(atcoder_id)
    )

    if(data['Count'] == 1):
        return True
    else:
        return False