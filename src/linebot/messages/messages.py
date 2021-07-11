
def atcoder_id_is_not_exist(atcoder_id):
    return atcoder_id + "さんは存在しないユーザーです"

def how_to_regist_stalkinglist():
    return "AtCoder Idをキーボードから入力してください\n※英大文字小文字は正しくご入力ください"

def how_to_delete_stalkinglist():
    return "ストーキングリストから削除するには、すでに登録されているAtCoder Idをキーボードから入力してください";

def invalid():
    return "AtCoderのIDを正しく入力してください(半角英数字)"

def no_stalking():
    return "ストーキングリストへの登録はまだありません"

def already_stalking(atcoder_id):
    return atcoder_id + "さんはすでにストーキングリストへ登録されています"

def regist_stalking_list(atcoder_id):
    return atcoder_id + "さんをストーキングリストへ登録しました"

def already_deleted(atcoder_id):
    return atcoder_id + "さんはすでにストーキングリストから削除されています"

def delete_stalking_list(atcoder_id):
    return atcoder_id + "さんをストーキングリストから削除しました"

def how_to_use_atcoder_stalker():
    res = """\
気になるあの子やライバルたちの精進をチェックしよう！\n
知りたいユーザーのAtCoder IDをキーボードから送信すると、ストーキングリストへ登録できます。
そのユーザーが精進したら通知が来ます。
※英大文字小文字は正しくご入力ください。
現在は9:00と20:00に通知を送っています。\n
既にストーキングリストに登録されているAtCoder IDを送信すると、ストーキングリストから削除できます。\n
「ストーキングリスト」ボタンを押すと現在のストーキングリストへの登録状況が分かります。\n
ご質問やバグ等ございましたら、twitterにてご連絡お願いいたします。\n
https://twitter.com/zaurus_yusya"; """

    return res