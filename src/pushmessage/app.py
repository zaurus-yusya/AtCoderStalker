import json
import urllib.request
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, PostbackEvent, FollowEvent, UnfollowEvent)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
import os
import sys
import logging
import boto3
from boto3.dynamodb.conditions import Key
import datetime

#他ファイルimport
import commonfunctions
import dynamodbfunctions

dynamodb = boto3.resource('dynamodb')

#channelの環境変数読み込み
channel_access_token = os.environ["ACCESS_TOKEN"]
#値がなかったら実行終了
if channel_access_token is None:
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

def lambda_handler(event, context):
    #現在時刻の取得
    now_datetime = datetime.datetime.now() + datetime.timedelta(hours=9)
    now_datetime_string = now_datetime.strftime("%Y/%m/%d %H:%M")
    print("現在時刻取得")
    #前回送った時刻の取得
    last_sent_time = dynamodbfunctions.get_last_sent_time()
    print("last time sent取得")

    #atcoder_infoのデータを取得
    atcoder_info_data = dynamodbfunctions.scan_atcoder_info()
    print("atcoder info table 取得")
    #全ユーザーのAC数取得(dict形式)
    all_users_accepted_count = commonfunctions.get_all_users_accepted_count()
    print("AC数 取得")
    #全ユーザーのRPS取得(dict形式)
    all_users_rated_point_sum = commonfunctions.get_all_users_rated_point_sum()
    print("RPS 取得")
    #line送信用のdict作成
    line_message_info = commonfunctions.create_line_message_info(atcoder_info_data, all_users_accepted_count, all_users_rated_point_sum)
    print("LINE message作成")
    
    #LINEuserテーブル取得
    line_user_data = dynamodbfunctions.scan_line_user()
    print("line user取得")

    #stalkingテーブル取得
    stalking_data = dynamodbfunctions.scan_stalking()
    print("stalking取得")
    #stalking dataをdictに変換
    stalking_data_dict = commonfunctions.create_stalking_data_dict(stalking_data)
    print("stalking dict取得")

    #メッセージ送信
    commonfunctions.send_line_message(line_user_data, stalking_data_dict, line_message_info, last_sent_time, now_datetime_string, line_bot_api)
    print("LINE MESSAGE 送信")

    #todo 現在時刻をテーブルへ挿入
    dynamodbfunctions.put_time_sent(now_datetime_string)
    print("現在時刻をテーブルに挿入")

    #todo atcoder info table に挿入
    dynamodbfunctions.put_atcoder_info(line_message_info)
    print("AtCoder Info更新完了")

    return{
        'statusCode': 200,
    }
