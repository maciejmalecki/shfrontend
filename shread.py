import serial
import datetime
import requests

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
url = 'http://localhost:8080'


while True:
	now = datetime.datetime.now()
	read_serial=ser.readline()
	msg = str(now) + ' ' +  read_serial
	print msg

	r = requests.post(url, data=msg)

