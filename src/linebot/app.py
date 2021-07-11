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

#他ファイルimport
from textmessage import textmessage 
from postbackevent import postbackevent
import dynamodbfunctions

dynamodb = boto3.resource('dynamodb')

#channelの環境変数読み込み
channel_secret = os.environ["CHANNEL_SECRET"]
channel_access_token = os.environ["ACCESS_TOKEN"]
#値がなかったら実行終了
if (channel_secret is None) or (channel_access_token is None):
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def lambda_handler(event, context):
    #署名の検証
    if "x-line-signature" in event["headers"]:
        signature = event["headers"]["x-line-signature"]
    elif "X-Line-Signature" in event["headers"]:
        signature = event["headers"]["X-Line-Signature"]
    body = event["body"]

    #テキストメッセージ受信時
    @handler.add(MessageEvent, message=TextMessage)
    def message(line_event):
        textmessage(line_event, line_bot_api)

    #ポストバック時
    @handler.add(PostbackEvent)
    def message(line_event):
        postbackevent(line_event, line_bot_api)

    #友だち追加時
    @handler.add(FollowEvent)
    def handle_follow(line_event):
        line_user_id = line_event.source.user_id
        #IDは昇順で連番　DBから割り振るユーザーIDを取得してから登録
        user_id = dynamodbfunctions.get_new_user_id(os.environ["LINE_USER_TABLE"])
        dynamodbfunctions.user_regist(line_user_id, user_id)

    #友だち削除・ブロック時
    @handler.add(UnfollowEvent)
    def handle_unfollow(line_event):
        line_user_id = line_event.source.user_id
        dynamodbfunctions.user_delete(line_user_id)

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        return{
            'statusCode': 400,
        }
    except InvalidSignatureError:
        return{
            'statusCode': 400,
        }
    return{
        'statusCode': 200,
    }
