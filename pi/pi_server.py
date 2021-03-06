# coding:utf-8
import httplib
import time
import urllib

import sonic

KEY = "GWD38ZF2B9G2MK0G"
headers = {"Content-type" : "application/x-www-form-urlencoded", "Accept" : "text/plain"}
ti = 10

if __name__ == "__main__":
	try:
		while True:
			dist = sonic.distance()
			if dist > 3000:
				continue

			params = urllib.urlencode({'field1': dist, 'key': KEY})
			conn = httplib.HTTPConnection("api.thingspeak.com:80")
			try:
				conn.request("POST", "/update", params, headers)
				response = conn.getresponse()
				print (response.status, response.reason)
			except :
				print ("Connection Failed")
			time.sleep(ti)

	except KeyboardInterrupt:
		sonic.GPIO.cleanup()
