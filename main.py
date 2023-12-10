import datetime
import requests
import json
import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import socket

def sendMessage(resultTextList,keyword):
    basic_send_url = 'https://kakaoapi.aligo.in/akv10/token/create/30/s/' # 요청을 던지는 URL, 현재는 토큰생성
    # token/create/토큰 유효시간/{y(년)/m(월)/d(일)/h(시)/i(분)/s(초)}/

    # ================================================================== 토큰 생성 필수 key값
    # API key, userid
    # API키, 알리고 사이트 아이디

    sms_data={'apikey': '7io1cogur7dgz4gany2dic1s0yzhvpkz', #api key
            'userid': 'quiz1010', # 알리고 사이트 아이디
    }

    create_token_response = requests.post(basic_send_url, data=sms_data)


    results=json.loads(create_token_response.text)
    pprint.pprint(results)

    #========주요변수
    apikey='7io1cogur7dgz4gany2dic1s0yzhvpkz'
    userid='quiz1010'
    token=results['token']
    plusid="@공생마케팅"
    phonenumber='01099323659'
    data = {
        'apikey': apikey,
        'userid': userid,
        'token': token,
        'plusid': plusid,
        'phonenumber': phonenumber,
    }

    response = requests.post('https://kakaoapi.aligo.in/akv10/profile/auth/', data=data)
    # print(response.text)

    data = {
        'apikey': apikey,
        'userid': userid,
        'token': token,
    }

    response = requests.post('https://kakaoapi.aligo.in/akv10/category/', data=data)
    # print(response.text)
    category=json.loads(response.text)
    # pprint.pprint(category)

    #=================
    category='016'
    #==============



    data = {
        'apikey': apikey,
        'userid': userid,
        'token': token,
    }

    response = requests.post('https://kakaoapi.aligo.in/akv10/profile/list/', data=data)
    data=json.loads(response.text)
    # print(data)
    #==================
    senderKey=data['list'][0]['senderKey']
    print("senderKey:",senderKey,"/ senderKey_TYPE:",type(senderKey),len(senderKey))




    data = {
        'apikey': apikey,
        'userid': userid,
        'token': token,
        'senderkey':senderKey,

    }

    response = requests.post('https://kakaoapi.aligo.in/akv10/template/list/', data=data)
    data=json.loads(response.text)
    # pprint.pprint(data)



    # =========톡 보내기
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    button_info = { 'button': [{
        'name': '시작 전 궁금해요',
        'linkType': 'WL',
        'linkTypeName': '웹링크',
        'linkPc': 'https://same-curve-e6b.notion.site/1-c45abc79fc674868a1e3790d972bb001?pvs=4',
        'linkMo' : 'https://same-curve-e6b.notion.site/1-c45abc79fc674868a1e3790d972bb001?pvs=4'
        },
        {'name': '진행 중 궁금해요',
        'linkType': 'WL',
        'linkTypeName': '웹링크',
        'linkPc': 'https://same-curve-e6b.notion.site/2-a3a9cdd013c14874b4eadf9672575436?pvs=4',
        'linkMo' : 'https://same-curve-e6b.notion.site/2-a3a9cdd013c14874b4eadf9672575436?pvs=4'
        },
        {'name': '당첨 후 궁금해요',
        'linkType': 'WL',
        'linkTypeName': '웹링크',
        'linkPc': 'https://same-curve-e6b.notion.site/3-9c2c04907571441f8909db61ec5fd1ad?pvs=4',
        'linkMo' : 'https://same-curve-e6b.notion.site/3-9c2c04907571441f8909db61ec5fd1ad?pvs=4'
        },
        {'name': '체험단시대 바로가기',
        'linkType': 'WL',
        'linkTypeName': '웹링크',
        'linkPc': 'https://www.allinonesite.co.kr/',
        'linkMo' : 'https://www.allinonesite.co.kr/'
        }
        ]
                    }
    button_info = json.dumps(button_info) # button의 타입은 JSON 이어야 합니다.
    
    
    innerContents=""

    try:
        key1=resultTextList[0].split(",")[0]
    except:
        key1=""
    print("key1:",key1)
    try:
        key2=resultTextList[1].split(",")[0]
    except:
        key2=""
    print("key2:",key2)
    try:
        key3=resultTextList[2].split(",")[0]
    except:
        key3=""
    print("key3:",key3)
    try:
        key4=resultTextList[3].split(",")[0]
    except:
        key4=""
    print("key4:",key4)
    try:
        key5=resultTextList[4].split(",")[0]
    except:
        key5=""
    print("key5:",key5)
    try:
        key6=resultTextList[5].split(",")[0]
    except:
        key6=""
    print("key6:",key6)
    try:
        key7=resultTextList[6].split(",")[0]
    except:
        key7=""
    print("key7:",key7)
    try:
        key8=resultTextList[7].split(",")[0]
    except:
        key8=""
    print("key8:",key8)
    try:
        key9=resultTextList[8].split(",")[0]
    except:
        key9=""
    print("key9:",key9)

    try:
        value1=resultTextList[0].split(",")[1]
    except:
        value1=""
    print("value1:",value1)
    try:
        value2=resultTextList[1].split(",")[1]
    except:
        value2=""
    print("value2:",value2)
    try:
        value3=resultTextList[2].split(",")[1]
    except:
        value3=""
    print("value3:",value3)
    try:
        value4=resultTextList[3].split(",")[1]
    except:
        value4=""
    print("value4:",value4)
    try:
        value5=resultTextList[4].split(",")[1]
    except:
        value5=""
    print("value5:",value5)
    try:
        value6=resultTextList[5].split(",")[1]
    except:
        value6=""
    print("value6:",value6)
    try:
        value7=resultTextList[6].split(",")[1]
    except:
        value7=""
    print("value7:",value7)
    try:
        value8=resultTextList[7].split(",")[1]
    except:
        value8=""
    print("value8:",value8)
    try:
        value9=resultTextList[8].split(",")[1]
    except:
        value9=""
    print("value9:",value9)


#     innerContents='''
# 1.{} / {}
# 2.{} / {}
# 3.{} / {}
# 4.{} / {}
# 5.{} / {}
# 6.{} / {}
# 7.{} / {}
# 8.{} / {}
# 9.{} / {}
# '''.format(key1,value1,key2,value2,key3,value3,key4,value4,key5,value5,key6,value6,key7,value7,key8,value8,key9,value9)
    for index,resultText in enumerate(resultTextList):
        firstText=resultText.split(",")[0]
        if len(firstText)>100:
            firstText=firstText[:100]+"..."
        text="{}.{} / {}".format(index+1,firstText,resultText.split(",")[1])
        innerContents=innerContents+text+'\n'
    print("길이는:")
    print(len(innerContents))
    # innerContents='중재김밥/https://www.naver.com'
    
    data = {
        'apikey': apikey,
        'userid': userid,
        'token': token,
        'senderkey': senderKey,
        'tpl_code':'TP_8433',
        'sender':phonenumber,
        # 'receiver_1':'01090703001',
        'receiver_1':"0"+str(keyword['전화번호']),
        'subject_1':'공생2',
        'message_1':'''안녕하세요. {} 고객님.\n
체험단시대입니다.
고객님께서 문의하신 카테고리의 체험단 소식 송신드립니다.\n
{}
※ 해당 메시지는 고객님께서 요청하신 체험단 조건에 해당하는 제안이 등록될 경우 발송됩니다 '''.format(keyword['이름'],innerContents),
        'button_1': button_info
    }

    print("메세지 데이타")
    pprint.pprint(data)
    print("data['message_1']:",data['message_1'],"/ data['message_1']_TYPE:",type(data['message_1']),len(data['message_1']))
    response = requests.post('https://kakaoapi.aligo.in/akv10/alimtalk/send/', headers=headers, data=data)
    data=json.loads(response.text)
    pprint.pprint(data)

def GetGoogleSpreadSheet():
    scope = 'https://spreadsheets.google.com/feeds'
    json = 'credential.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
    gc = gspread.authorize(credentials)
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Mg3HSTHCXBNAuIjn4oEu01KFaW3VAhCwJnM29752jYI/edit#gid=0'
    doc = gc.open_by_url(sheet_url)
    worksheet = doc.worksheet('시트1')
    #=================특정행의 정보 가져오기
    # cell_data = worksheet.acell('A1').value
    #=================전체정보가져오기
    all_data=worksheet.get_all_records()
    #==================맨 밑행에 데이타 넣기
    # new_row = ['John', 30, 'Teacher']
    # worksheet.append_row(new_row)
    # pprint.pprint(all_data)
    return all_data

def search(keywordList1,keywordList2,sorting,dday):
    url = 'https://f36dcjopejicrmfh3tq2bavmbe0ljydb.lambda-url.ap-northeast-2.on.aws/search'
    print("url:", url)
    data={
    'keywords1': keywordList1,
    'keywords2': keywordList2,
    }
    print('data:',data)
    res = requests.post(url, data=json.dumps(data))
    res.raise_for_status()
    print('status_code:',res.status_code)
    results = json.loads(res.text)
    if sorting=="기한적은순":
        results = sorted(results, key=lambda x: int(x['dday']))
    else:
        results = sorted(results, key=lambda x: int(x['dday']),reverse=True)
    with open('results.json', 'w',encoding='utf-8-sig') as f:
        json.dump(results, f, indent=2,ensure_ascii=False)
    pprint.pprint(results)
    
    resultTextList=[]
    for result in results:
        # print("===============")
        # pprint.pprint(result)
        # print("===============")
        if len(result['url'])>=5:
            resultText=result['title'].replace("\n","").replace("  ","")+","+result['url']
            resultTextList.append(resultText)
        else:
            pass
    resultTextList=resultTextList[:6]
    print(len(resultTextList))
    print("===============")
    pprint.pprint(resultTextList)
    print("===============")
    # print("작업완료")
    resultTextList=resultTextList[:9]

    return resultTextList

def doRun():
    keywordList=GetGoogleSpreadSheet()
    for index, keyword in enumerate(keywordList):
        print('이름:',keyword['이름'])
        keyword1 = keyword['지역'].split(",")
        keyword2 = keyword['관심카테고리'].split(",")
        sorting = '기한적은순'
        dday = 9999
        try:
            resultTextList = search(keyword1, keyword2, sorting, dday)
        except:
            print('에러발생으로건너뜀')
            continue
        if len(resultTextList)>=1:
            print("결과있음")
            sendMessage(resultTextList, keyword)
        else:
            print("결과없음")
    print("실행완료!")



# startFlag=False
# while True:
#     timeNow=datetime.datetime.now().strftime("%H")
#     try:
#         keywordList=GetGoogleSpreadSheet()
#         if int(keywordList[0]['발송시간'])==int(timeNow) and startFlag==False:
#             print("시간맞음")
#         #     for index, keyword in enumerate(keywordList):
#         #         keyword1 = keyword['지역'].split(",")
#         #         keyword2 = keyword['관심카테고리'].split(",")
#         #         sorting = '기한적은순'
#         #         dday = 9999
#         #         resultTextList = search(keyword1, keyword2, sorting, dday)
#         #         sendMessage(resultTextList, keyword)
#             startFlag=True
#         else:
#             print("시간안맞음")
#     except:
#         print("에러로잠깐쉼")
#         time.sleep(60)
#     if int(timeNow)==0:
#         startFlag=False
#     ipaddress=socket.gethostbyname(socket.gethostname())
#     print("ipaddress:",ipaddress,"/ ipaddress_TYPE:",type(ipaddress),len(ipaddress))
#     timeNow=datetime.datetime.now().strftime("%Y년%m월%d일_%H시%M분%S초")
#     print("timeNow:",timeNow,"/ timeNow_TYPE:",type(timeNow))
#     time.sleep(0.1)


# 크론 표현식으로 함수를 예약합니다. (예: 매일 오후 3시)
# keywordList=GetGoogleSpreadSheet()
# reserveTime="{}:00".format(keywordList[0]['발송시간'])
# schedule.every(reserveTime).day.at().do(doRun())
# print("reserveTime:",reserveTime,"/ reserveTime_TYPE:",type(reserveTime),len(reserveTime))
# while True:
#     schedule.run_pending()
#     time.sleep(10)


keywordList=GetGoogleSpreadSheet()
# 크론 표현식으로 함수를 예약합니다. (예: 매일 오후 3시)
while True:
    timeNowString=datetime.datetime.now().strftime("%H%M%S")
    # timeTarget=datetime.datetime.now().strftime("%Y%m%d_{}{}{}".format(keywordList[0]['발송시간'],'00','00'))
    timeNow=datetime.datetime.now()
    timeTarget=dt = datetime.datetime(timeNow.year,timeNow.month,timeNow.day,keywordList[0]['발송시간'], 0, 0).strftime("%H%M%S")
    text="현재:{}/{}".format(timeNowString,timeTarget)
    print(text)
    if timeNowString==timeTarget:
    # if True:
        doRun()
    time.sleep(1)
