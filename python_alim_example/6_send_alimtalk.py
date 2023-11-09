# -*- coding: utf-8 -*-
import requests
import json

basic_send_url = 'https://kakaoapi.aligo.in/akv10/alimtalk/send/' # 요청을 던지는 URL, 알림톡 전송


# ================================================================== 알림톡 보낼 때 필수 key값
# API key, userid, token, senderkey, tpl_code, sender, receiver_1, subject_1, message_1
# API키, 알리고 사이트 아이디, 토큰, 발신프로파일 키, 템플릿 코드, 발신번호, 수신번호, 알림톡 제목, 알림톡 내용
# 
# ================================================================== 알림톡 보낼 때 선택 key값
# senddate, recvname_1, button_1, failover, fsubject_1, fmessage_1, testMode
# 예약일, 수신자 이름, 버튼 정보, 실패시 대체문자 {전송여부/제목/내용}, 테스트 모드 적용 여부(기본N)
#


# -------------------------------------------------------------------------------------------------
# BUTTON
#
# name: 버튼명, 
# linkType: 버튼 링크타입(DS:배송조회, WL:웹링크, AL:앱링크, BK:봇키워드, MD:메시지전달),
# linkTypeName : 버튼 링크 타입네임, ( 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개) 
# linkM: 모바일 웹링크주소(WL일 때 필수), linkP: PC웹링크 주소(WL일 때 필수),
# linkI: IOS앱링크 주소(AL일 때 필수), linkA: Android앱링크 주소(AL일 때 필수)

button_info = {'button': [{'name':'name', # 버튼명
                        'linkType':'WL', # DS, WL, AL, BK, MD
                        'linkTypeName' : '웹링크', # 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개
                        #'linkM':'mobile link', # WL일 때 필수
                        #'linkP':'pc link', # WL일 때 필수
                        #'linkI': 'IOS app link', # AL일 때 필수
                        #'linkA': 'Android app link' # AL일 때 필수
                }]}


''' 만약 button이 여러개이면, 'button'key의 value list에 버튼 개수만큼 dict를 추가해주시면 됩니다.
button_info = {'button': [{'name':'1번버튼', ~}, {'name':'2번버튼', ~}, {'name':~}]} '''


button_info = json.dumps(button_info) # button의 타입은 JSON 이어야 합니다.


sms_data={'apikey': 'xxxxxxxxxxxx', #api key
        'userid': 'xxxxxxxxxxxx', # 알리고 사이트 아이디
        'token': 'xxxxxxxxxxxx', # 생성한 토큰
        'senderkey': 'xxxxxxxxxxxx', # 발신프로파일 키
        'tpl_code': 'xxxxxxxxxxxx', # 템플릿 코드
        'sender' : '01000000000', # 발신자 연락처,
        #'senddate': '19000131120130', # YYYYMMDDHHmmss
        'receiver_1': '01000000000', # 수신자 연락처
        #'recvname_1': '홍길동1', # 수신자 이름
        'subject_1': '알림톡 제목', # 알림톡 제목 - 수신자에게는 표기X
        'message_1': '알림톡 내용', # 알림톡 내용 - 등록한 템플릿이랑 개행문자 포함 동일하게 입력.
        'button_1': button_info, # 버튼 정보
        #'failover': 'Y or N', # 실패시 대체문자 전송 여부(템플릿 신청시 대체문자 발송으로 설정하였더라도 Y로 입력해야합니다.)
        #'fsubject_1': '대체문자 제목', # 실패시 대체문자 제목
        #'fmessage_1': '대체문자 내용', # 실패시 대체문자 내용
        #'testMode': 'Y or N' # 테스트 모드 적용여부(기본N), 실제 발송 X
        }

alimtalk_send_response = requests.post(basic_send_url, data=sms_data)

print(alimtalk_send_response.json())
