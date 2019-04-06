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

