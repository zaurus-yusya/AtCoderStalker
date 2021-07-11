import requests
import json

def get_all_users_rated_point_sum():
    #全ユーザーのRPS取得
    url = 'https://kenkoooo.com/atcoder/resources/sums.json'
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    #dict形式に変換
    dict_data = {}
    for item in data:
        dict_data[item["user_id"]] = item["point_sum"]

    return dict_data