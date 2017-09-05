import sys
import httplib, urllib


def weater(appKey, lan, lon):
    appKey = "e1e427d8-c745-3632-be37-3416876bf0bb"
    headers = {"Content-type" : "application/json;charset=UTF-8", "Accept" : "application/json"}

    url = "http://apis.skplanetx.com/weather/current/hourly?version=1&lat=" + lan + "&lon=" + lon + "&appKey=" + appKey

    encodingUrl = urllib.urlencode(url)
    conn = httplib.HTTPConnection(encodingUrl)

    try:
        conn.request("GET", headers)
        response = conn.getresponse()
        print response
    except:
        print "Connection Failed"

weater("e1e427d8-c745-3632-be37-3416876bf0bb", "37.4870600000", "127.0460400000")