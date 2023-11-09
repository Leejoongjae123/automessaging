# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/template/add/' # 요청을 던지는 URL, 템플릿 생성

# ================================================================== 템플릿 생성할 때 필수 key값
# API key, userid, token, senderkey, tpl_name, tpl_content
# API키, 알리고 사이트 아이디, 토큰, 발신프로파일 키, 템플릿 이름, 템플릿 내용
# 
# ================================================================== 템플릿 생성할 때 선택 key값
# tpl_button
# 템플릿 버튼
#


''' 발송할 때마다 변경되는 부분은 변수처리하시면 됩니다. #{변수명}
 ex) 'linkP' : 'http://#{pc 링크}', 'tpl_content': '안녕하세요. #{고객명}님.'''


# -------------------------------------------------------------------------------------------------
# BUTTON
#
# name: 버튼명
# linkType: 버튼 링크타입(DS:배송조회, WL:웹링크, AL:앱링크, BK:봇키워드, MD:메시지전달),
# linkTypeName : 버튼 링크 타입네임, ( 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개) 
# linkM: 모바일 웹링크주소(WL일 때 필수), linkP: PC웹링크 주소(WL일 때 필수),
# linkI: IOS앱링크 주소(AL일 때 필수), linkA: Android앱링크 주소(AL일 때 필수)

button_info = {'button': [{'name':'button name', # 버튼명
                        'linkType':'link type', # DS, WL, AL, BK, MD
                        #'linkTypeName' : '웹링크', # 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개
                        #'linkM':'mobile link', # WL일 때 필수
                        #'linkP':'pc link', # WL일 때 필수
                        #'linkI': 'IOS app link', # AL일 때 필수
                        #'linkA': 'Android app link' # AL일 때 필수
                }]}


''' 만약 button이 여러개이면, 'button'key의 value list에 버튼 개수만큼 dict를 추가해주시면 됩니다.
button_info = {'button': [{'name':'1번버튼', ~}, {'name':'2번버튼', ~}, {'name':~}]} '''


button_info = json.dumps(button_info) # button의 타입은 JSON 이어야 합니다.


sms_data={'apikey': 'xxxxxx', #api key
        'userid': 'xxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxxxxxxxx', # 생성한 토큰
        'senderkey': 'xxxxxxxxxxxx', # 발신프로파일 키
        'tpl_name': 'template 이름', # 템플릿 이름
        'tpl_content': 'template 내용', # 템플릿 내용
        #'tpl_button': button_info # 버튼 사용할 경우 템플릿 버튼
}

create_template_response = requests.post(basic_send_url, data=sms_data)

print(create_template_response.json())
