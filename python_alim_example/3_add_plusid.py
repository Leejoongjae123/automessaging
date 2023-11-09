# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/profile/add/' # 요청을 던지는 URL, 친구등록 심사요청

# ================================================================== 심사요청할 때 필수 key값
# API key, userid, token, plusid, authnum, phonenumber, categorycode
# API키, 알리고 사이트 아이디, 토큰, 카카오채널 아이디, senderkey, 관리자 핸드폰 번호, 카테고리 코드

sms_data={'apikey': 'xxxxxxxxxxxx', #api key
        'userid': 'xxxxxxxxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxxxxxxxx', # 생성한 토큰
        'plusid': '@xxx', # 카카오채널 아이디(@포함)
        'authnum': 'xxxxxxxxxxxx', # 발신프로필 인증번호(senderkey)
        'phonenumber': '01000000000', # 카카오채널 알림받는 관리자 핸드폰 번호
        'categorycode': '0000000000' # 발신프로필의 카테고리 코드 - 카테고리 조회로 확인
}

request_enrollment_response = requests.post(basic_send_url, data=sms_data)

print(request_enrollment_response.json())
