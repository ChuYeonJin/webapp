# coding:utf-8
import json
import requests

params ={"version" : "1", "city" : "부산", "country" : "수영구", "village" : "광안동"}
headers = {"appKey" : "e1e427d8-c745-3632-be37-3416876bf0bb"}
url = "http://apis.skplanetx.com/weather/current/hourly"

r = requests.get(url, params=params, headers=headers)
print (r.json())