def create_stalking_data_dict(stalking_data):
    stalking_data_dict = {}
    for item in stalking_data:
        user_id = int(item["user_id"])     #Decimal型をint型に変更
        atcoder_id = item["atcoder_id"]
        if(user_id in stalking_data_dict):
            stalking_data_dict[user_id].append(atcoder_id)
        else:
            stalking_data_dict[user_id] = []
            stalking_data_dict[user_id].append(atcoder_id)
    return stalking_data_dict