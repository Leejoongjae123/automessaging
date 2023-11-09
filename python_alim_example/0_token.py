# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/token/create/30/s/' # 요청을 던지는 URL, 현재는 토큰생성
# token/create/토큰 유효시간/{y(년)/m(월)/d(일)/h(시)/i(분)/s(초)}/

# ================================================================== 토큰 생성 필수 key값
# API key, userid
# API키, 알리고 사이트 아이디

sms_data={'apikey': 'xxxxxxxxxxxx', #api key
        'userid': 'xxxxxxxxxxxx', # 알리고 사이트 아이디
}

create_token_response = requests.post(basic_send_url, data=sms_data)


print(create_token_response.json())