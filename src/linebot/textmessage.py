import re
#from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

import commonfunctions
import dynamodbfunctions
import messages

def textmessage(line_event, line_bot_api):
    line_user_id = line_event.source.user_id
    text = line_event.message.text

    #textがatcoderIDかチェック
    if(re.match('^[0-9a-zA-Z_]+$', text)):
        #atcoderが存在するか調べる
        if(commonfunctions.is_atcoder_id_exist(text)):
            #既にストーキングリストに登録されているか調べる
            #user_idの取得
            user_id = dynamodbfunctions.get_user_id(line_user_id)

            #stalkingリストにすでに登録済みかチェック
            if(dynamodbfunctions.is_already_stalking(user_id, text) == False):
                confirm_message = commonfunctions.make_confirm_button(text, 'regist')
            else:
                confirm_message = commonfunctions.make_confirm_button(text, 'delete')
            
            line_bot_api.reply_message(line_event.reply_token, confirm_message)
        else:
            message = messages.atcoder_id_is_not_exist(text)
            line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))

    elif(text == "登録方法"):
        message = messages.how_to_regist_stalkinglist()
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))

    elif(text == "削除方法"):
        message = messages.how_to_delete_stalkinglist()
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))

    elif(text == "リスト"):
        #user_idの取得
        user_id = dynamodbfunctions.get_user_id(line_user_id)

        #ストーキングリストの取得
        stalking_list = dynamodbfunctions.get_stalking_list(user_id)

        message = ""
        if len(stalking_list) == 0:
            #0人の場合、ストーキングリストへの登録がまだ無い旨を送信
            message = messages.no_stalking()
        else:
            #ストーキングリストの一覧を作成
            for item in stalking_list:
                message += "\n" + item["atcoder_id"]
            message = "現在" + str(len(stalking_list)) + "人登録されています" + message

        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))

    elif(text == "使い方"):
        message = messages.how_to_use_atcoder_stalker()
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))

    else:
        #adminfunction
        message = messages.invalid()
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))