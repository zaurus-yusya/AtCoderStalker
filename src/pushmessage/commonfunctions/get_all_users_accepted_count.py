import requests
import json

def get_all_users_accepted_count():
    #全ユーザーのAC数取得
    url = 'https://kenkoooo.com/atcoder/resources/ac.json'
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    #dict形式に変換
    dict_data = {}
    for item in data:
        dict_data[item["user_id"]] = item["problem_count"]

    return dict_data