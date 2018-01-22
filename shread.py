import serial
import datetime
import requests
import logging, logging.handlers

LOG_FILE_NAME='log/shread.log'

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.handlers.TimedRotatingFileHandler(LOG_FILE_NAME, when='midnight', backupCount=5)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger = logging.getLogger('shread')
logger.propagate = False
logger.addHandler(fh)

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
url = 'http://localhost:8080'


while True:
	now = datetime.datetime.now()
	read_serial=ser.readline()
	msg = str(now) + ' ' +  read_serial
	logger.debug(msg)

	r = requests.post(url, data=msg)

