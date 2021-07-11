import requests

def is_atcoder_id_exist(atcoder_id):
    res = requests.get('https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user=' + atcoder_id)
    if(res.status_code == 200):
        return True
    else:
        return False


