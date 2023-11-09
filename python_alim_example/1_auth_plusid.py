# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/profile/auth/' # 요청을 던지는 URL, 현재는 카카오채널 인증

# ================================================================== 채널인증 필수 key값
# API key, userid, token, plusid, phonenumber
# API키, 알리고 사이트 아이디, 토큰, 카카오채널 아이디, 관리자 핸드폰 번호

sms_data={'apikey': 'xxxxxxxxxxxx', #api key
        'userid': 'xxxxxxxxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxx', # 생성한 토큰
        'plusid': 'xxxxxxxxxxxx', # 카카오채널 아이디(@포함)
        'phonenumber': '01000000000' # 카카오채널 알림받는 관리자 핸드폰 번호
}

channel_auth_response = requests.post(basic_send_url, data=sms_data)

print(channel_auth_response.json())
