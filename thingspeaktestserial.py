import httplib, urllib
import time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
def loop():
	x = ser.readline()
	params = urllib.urlencode({'field1': x,'key':'Your_API_Write_Key'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"
  
if __name__ == "__main__":
        while True:
                loop()
                time.sleep(16)
