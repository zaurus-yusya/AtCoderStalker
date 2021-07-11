import re
#from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

import dynamodbfunctions
import messages

def postbackevent(line_event, line_bot_api):
    line_user_id = line_event.source.user_id
    postback_data = line_event.postback.data  #"regist=Zaurus", "delete=Zaurus"
    method = postback_data.split('=')[0]
    atcoder_id = postback_data.split('=')[1]
    user_id = dynamodbfunctions.get_user_id(line_user_id)

    if method == "regist":
        #既に登録されているか確認　登録されていたら既に登録されている旨を返信して終了
        if dynamodbfunctions.is_already_stalking(user_id, atcoder_id):
            message = messages.already_stalking(atcoder_id)
            line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))
            return

        #登録する
        dynamodbfunctions.regist_stalking_list(user_id, atcoder_id)
        message = messages.regist_stalking_list(atcoder_id)
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))
        
        #初めてのatcoder idの場合DBに登録
        if dynamodbfunctions.is_first_time_regist_atcoder_id(atcoder_id) == False:
            dynamodbfunctions.regist_atcoder_info(atcoder_id)

    elif method == "delete":
        #既に削除されているか確認　削除されていたら既に削除されている旨を返信して終了
        if dynamodbfunctions.is_already_stalking(user_id, atcoder_id) == False:
            message = messages.already_deleted(atcoder_id)
            line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))
            return

        #削除する
        dynamodbfunctions.delete_stalking_list(user_id, atcoder_id)
        message = messages.delete_stalking_list(atcoder_id)
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=message))
        return