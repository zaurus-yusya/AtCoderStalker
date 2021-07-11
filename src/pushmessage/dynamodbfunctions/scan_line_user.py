import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def scan_line_user():
    TABLE = dynamodb.Table(os.environ["LINE_USER_TABLE"])

    data = TABLE.scan()
    
    return data['Items']