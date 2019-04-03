import requests
import datetime
import json

url = 'http://www.way2sms.com/api/v1/sendCampaign'
file_name = 'start_up_log.txt'

def file_write():
	file = open(file_name, 'w')
	phone_number = str(raw_input('Enter phone number: '))
	api_key = str(raw_input('Enter API-Key: '))
	api_secret = str(raw_input('Enter API-Secret: '))
	sender_id = str(raw_input('Enter Sender ID: '))
	data = { 'Phone Number': phone_number, 'API-Key': api_key, 'API-Secret': api_secret, 'Sender ID': sender_id }
	data = json.dumps(data)
	file.write(data)
	file.close()
	return data

def file_read():
	file = open(file_name, 'r')
	data = file.read()
	if len(data) == 0:
		file_write()
	else:
		data = json.loads(data)
	file.close()
	return data

data = file_read()

api_key = data
secret = 'AQM5HJ3OZR5AVDBX'
use_type = 'prod'
phone_no = '9717271991'
sender_id = 'active-sender-id'
message = 'Computer turned on at ' + str(datetime.datetime.now())


req_params = {
  'apikey':api_key,
  'secret':secret,
  'usetype':use_type,
  'phone': phone_no,
  'message':message,
  'senderid':sender_id
}

# send_message = requests.post(url, req_params)
# print send_message.json


