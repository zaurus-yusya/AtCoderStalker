import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

def send_line_message(line_user_data, stalking_data_dict, line_message_info, last_sent_time, now_datetime_string, line_bot_api):

    send_message_num = 0      #メッセージを送った数
    inactive_user = 0         #友達登録してるけどストーキングリストに登録していない人
    
    for line_user_item in line_user_data:
        send_message = ""
        line_user_id = line_user_item["line_user_id"]
        user_id = int(line_user_item["user_id"])      #Decimal型をint型に変更

        try:
            for stalking_user in stalking_data_dict[user_id]:
                try:
                    if(line_message_info[stalking_user]["new_ac"] > 0):
                        send_message += (stalking_user + "さんが" + str(line_message_info[stalking_user]["new_ac"]) + "問ACしました！\n合計"+ str(line_message_info[stalking_user]["accepted_count"]) + "問AC！ " + '{:,}'.format(line_message_info[stalking_user]["rated_point_sum"]) + "RPSを獲得！" + "\n\n")
                except KeyError as e:
                    print("catch KeyError" + str(e))
            send_message = send_message[:-2]   #最後の改行文字を削除

            #LINEにメッセージ送信
            if(send_message != ""):
                try:
                    now_datetime_string = now_datetime_string[5:] # 2020/06/07 01:19 → 06/07 01:19
                    #send_message =  last_sent_time + "から" + now_datetime_string + "までの間\n" + send_message
                    send_message =  last_sent_time + "から今までの間に\n" + send_message
                    line_bot_api.push_message(line_user_id, TextSendMessage(text=send_message))
                    print(str(user_id) + "さんにLINEメッセージを送信しました。")
                    send_message_num += 1
                except LineBotApiError as e:
                    print(e)

        except KeyError as e:
            print(str(user_id) + "さんはストーキングリストに誰も登録していません。")
            inactive_user += 1

    try:
        admin_send_message = str(send_message_num) + "通のメッセージを送信しました\nInactiveユーザーは" + str(inactive_user) + "人です"
        line_bot_api.push_message(os.environ["ADMIN_USER_ID"], TextSendMessage(text=admin_send_message))
        print("Admin Messageを送信しました")
    except LineBotApiError as e:
        print(e)