import re
import requests

s = 'Zaurus'
res = requests.get('https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user=' + s)

print(res.status_code)
print(res.json()['count'])

res = requests.get('https://kenkoooo.com/atcoder/resources/sums.json')

data = res.json()
rps = -1
for item in data:
    if item['user_id'] == s:
        rps = int(item['point_sum'])
        break

print(rps)