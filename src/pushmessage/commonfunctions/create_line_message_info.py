def create_line_message_info(items, all_users_accepted_count, all_users_rated_point_sum):
    dict_line_message = {}
    for item in items:
        db_atcoder_id = item["atcoder_id"]
        db_accepted_count = item["accepted_count"]
        try:
            db_new_ac = item["new_ac"]
        except KeyError as e:
            print("new_acがまだありません　0に設定します")
            db_new_ac = 0

        #現在情報の取得
        try:
            now_accepted_count = all_users_accepted_count[db_atcoder_id]
            now_new_ac = now_accepted_count - db_accepted_count
            now_rated_point_sum = all_users_rated_point_sum[db_atcoder_id]

            # #初回登録された直後だとdb_accepted_countが-1になってるので、そのときはnow_new_acを-1とする
            # if db_accepted_count == -1:
            #     now_new_ac = -1

            dict_line_message[db_atcoder_id] = {"accepted_count": now_accepted_count, "new_ac": int(now_new_ac), "rated_point_sum": int(now_rated_point_sum)}
        except KeyError as e:
            print("catch KeyError" + str(e))

    return dict_line_message