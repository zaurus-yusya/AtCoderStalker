import os
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def put_atcoder_info(line_message_info):
    TABLE = dynamodb.Table(os.environ["ATCODER_INFO_TABLE"])

    for atcoder_id in line_message_info:
        accepted_count = line_message_info[atcoder_id]["accepted_count"]
        new_ac = line_message_info[atcoder_id]["new_ac"]
        rated_point_sum = line_message_info[atcoder_id]["rated_point_sum"]

        #dictのnew_acが0以外のものをputする(0だとDBの内容が書き変わらないため)
        if(new_ac != 0):
            TABLE.put_item(
                Item={
                    "atcoder_id": atcoder_id,
                    "accepted_count": accepted_count,
                    "new_ac": new_ac,
                    "rated_point_sum": rated_point_sum
                }
            )
            print("succeed put DB " + str(atcoder_id))