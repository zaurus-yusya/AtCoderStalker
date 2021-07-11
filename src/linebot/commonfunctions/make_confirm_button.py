from linebot.models import (TemplateSendMessage, ConfirmTemplate, PostbackAction)

def make_confirm_button(atcoder_id, method):

    if method == 'regist':
        message = 'さんをストーキングリストに登録しますか？'
    else:
        message = 'さんはすでに登録されています。\n削除しますか？'

    confirm_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text=atcoder_id + message,
            actions=[
                PostbackAction(
                    label='Yes',
                    data=method + '=' + atcoder_id
                ),
                PostbackAction(
                    label='No',
                    data='none' + '=' + atcoder_id
                )
            ]
        )
    )

    return confirm_message