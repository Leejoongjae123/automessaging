# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/category/' # 요청을 던지는 URL, 카카오채널 카테고리 조회

# ================================================================== 채널 카테고리 조회할 때 필수 key값
# API key, userid, token
# API키, 알리고 사이트 아이디, 토큰

sms_data={'apikey': 'xxxxxxxxxxxx', #api key
        'userid': 'xxxxxxxxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxx' # 생성한 토큰
}

category_search_response = requests.post(basic_send_url, data=sms_data)

print(category_search_response.json())
