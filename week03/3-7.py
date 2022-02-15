# import requests
# res = requests.get("http://www.naver.com")
# print("응답코드 :", res.status_code) # 200이면 정상 접근, 304이면 접근 권한이 없음

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# print(rjson['RealtimeCityAir']['row'][0]['MSRSTE_NM'])

gus =rjson['RealtimeCityAir']['row']

for gu in gus :
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if gu_mise < 100: #100보다 작은거
        print(gu_name,gu_mise)