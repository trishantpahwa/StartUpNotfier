import os
import json


def get_startup_location():
    start_up_sh = 'start_up.sh'
    start_up_location = '\\etc\\init.d\\' + start_up_sh
    try:
        with open(start_up_location, 'w') as start_up_file:
            with open(start_up_sh, 'r') as start_up:
                start_up_data = start_up.read()
                start_up_file.write(start_up_data)
    except IOError:
        print 'File not found.'

def install():
    start_up = 'startup.py'
    start_up_script = '\\usr\\share\\'
    if 'StartUpNotifier' not in os.listdir(start_up_script):
        os.mkdir(start_up_script + '\\StartUpNotifier')
    start_up_script += '\\StartUpNotifier\\' + start_up
    try:
        with open(start_up_script, 'w') as start_up_file:
            with open(start_up, 'r') as start_up:
                start_up_data = start_up.read()
                start_up_file.write(start_up_data)
    except IOError:
        print 'File not found'

def file_write():
    file_location = '\\usr\\share\\StartUpNotifier\\'
    file_name = file_location + 'start_up_log.txt'
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

def install_StartUpNotifier():
    install()
    file_write()
    get_startup_location()

if __name__ == '__main__()':
    install_StartUpNotifier()