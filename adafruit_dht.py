import Adafruit_DHT
import sys
import time
import httplib, urllib

KEY = "GWD38ZF2B9G2MK0G"
headers = {"Content-type" : "application/x-www-form-urlencoded", "Accept" : "text/plain"}

ti = 10

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

if __name__ == "__main__":
    try:
        while True:

            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            param = [temperature, humidity]

            for i in range(0, 2):
                params = urllib.urlencode({'field'+str(i+1) : param[i], 'key': KEY})
                conn = httplib.HTTPConnection("api.thingspeak.com:80")

                try:
                    conn.request("POST", "/update", params, headers)
                    response = conn.getresponse()
                    print "field%d" %(i+1), " : ", param[i], response.status, response.reason
                except:
                    print "Connection Failed"
            time.sleep(ti)

    except KeyboardInterrupt:
        sys.exit(1)