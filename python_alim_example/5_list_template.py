# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/template/list/' # 요청을 던지는 URL, 등록된 템플릿 리스트

# ================================================================== 템플릿 리스트 조회할 때 필수 key값
# API key, userid, token, senderkey
# API키, 알리고 사이트 아이디, 토큰, 발신프로필 키

sms_data={'apikey': 'xxxxxx', #api key
        'userid': 'xxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxxxxxxxx', # 생성한 토큰
        'senderkey': 'xxxxxxxxxxxx' # 발신프로필 키
}

template_list_response = requests.post(basic_send_url, data=sms_data)

print(template_list_response.json())
