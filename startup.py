import requests
import datetime
import json
import sys
import os

url = 'http://www.way2sms.com/api/v1/sendCampaign'
file_name = 'start_up_log.txt'

def file_write():
	try:
		with open(file_name, 'w') as file:
			phone_number = str(raw_input('Enter phone number: '))
			api_key = str(raw_input('Enter API-Key: '))
			api_secret = str(raw_input('Enter API-Secret: '))
			sender_id = str(raw_input('Enter Sender ID: '))
			data = { 'Phone Number': phone_number, 'API-Key': api_key, 'API-Secret': api_secret, 		 'Sender ID': sender_id }
			file_data = json.dumps(data)
			file.write(file_data)
			return data
	except IOError:
		print IOError

def file_read():
	try:
		with open(file_name, 'r') as file:
			data = file.read()
			if len(data) == 0:
				file_write()
			else:
				data = json.loads(data)
			return data
	except IOError:
		print file_name + ' not found.'
		data = file_write()
		return data

def get_computer_details():
	platform = sys.platform
	username = os.system('whoami')
	data = { 'platform': platform, 'username': username }
	return data

if __name__ == '__main__':
	computer_data = get_computer_details()
	api_data = file_read()
	api_key = api_data['API-Key']
	secret = api_data['API-Secret']
	use_type = 'prod'
	phone_no = api_data['Phone Number']
	sender_id = api_data['Sender ID']
	message = 'Computer turned on at ' + str(datetime.datetime.now())

	req_params = {
  		'apikey': api_key,
  		'secret': secret,
  		'usetype': use_type,
  		'phone': phone_no,
  		'message': message,
  		'senderid': sender_id
	}


	#send_message = requests.post(url, req_params)
	#print send_message
	#print send_message.text
	#print send_message.status_code
	#print send_message.json
