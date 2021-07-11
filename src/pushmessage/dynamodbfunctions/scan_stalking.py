import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def scan_stalking():
    TABLE = dynamodb.Table(os.environ["STALKING_TABLE"])

    data = TABLE.scan()
    
    return data['Items']