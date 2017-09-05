# coding:utf-8
import json
import requests

params ={"version" : "1", "city" : "부산", "county" : "수영구", "village" : "광안동"}
headers = {"appKey" : "e1e427d8-c745-3632-be37-3416876bf0bb"}
url = "http://apis.skplanetx.com/weather/current/hourly"

r = requests.get(url, params=params, headers=headers)

data = json.loads(r.text)
weather = data["weather"]["hourly"]
cTime = weather[0]["timeRelease"]
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]

cWeather = "오늘의 날씨 " + cTime + " 기준 하늘은 " + cSky + "이고 풍속은 " + cWind + "이고 기온은 " + cTemp + "입니다."
print(cWeather)