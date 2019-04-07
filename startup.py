import requests
import datetime
import json
import sys
import os

url = 'http://www.way2sms.com/api/v1/sendCampaign'

def file_write(file_name):
	try:
		with open(file_name, 'w') as file:
			phone_number = str(raw_input('Enter phone number: '))
			api_key = str(raw_input('Enter API-Key: '))
			api_secret = str(raw_input('Enter API-Secret: '))
			data = { 'Phone Number': phone_number, 'API-Key': api_key, 'API-Secret': api_secret }
			file_data = json.dumps(data)
			file.write(file_data)
			return data
	except IOError, TypeError:
		print IOError
		print TypeError

def file_read(file_name):
	try:
		with open(file_name, 'r') as file:
			data = file.read()
			if len(data) == 0:
				file_write(file_name)
			else:
				data = json.loads(data)
			return data
	except IOError:
		print file_name + ' not found.'
		data = file_write(file_name)
		return data

def get_computer_details():
	platform = sys.platform
	username = os.getenv('username')
	version = sys.version
	arch = 'x' + version.split('bit')[0][-3:]
	data = { 'platform': platform, 'arch': arch, 'username': username }
	return data

if __name__ == '__main__':
	computer_data = get_computer_details()
	file_name = 'C:\\Users\\' + computer_data['username'] + '\\StartUpNotifier\\start_up_log.txt'
	api_data = file_read(file_name)
	api_key = api_data['API-Key']
	secret = api_data['API-Secret']
	use_type = 'prod'
	phone_no = api_data['Phone Number']
	sender_id = computer_data['username'] + '@' + computer_data['platform'] + \
				computer_data['arch']
	message = sender_id + 'turned on at ' + str(datetime.datetime.now())

	req_params = {
  		'apikey': api_key,
  		'secret': secret,
  		'usetype': use_type,
  		'phone': phone_no,
  		'message': message,
  		'senderid': sender_id
	}

	send_message = requests.post(url, req_params)
	status_code = send_message.status_code
	send_message = json.loads(send_message.text)
	code = send_message['code']
	if status_code == 200 and code == '200':
		print 'Message sent successfully.'