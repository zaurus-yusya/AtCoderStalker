import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def scan_atcoder_info():
    TABLE = dynamodb.Table(os.environ["ATCODER_INFO_TABLE"])

    data = TABLE.scan()
    
    return data['Items']