import os


def get_startup_location(username):
    start_up_bat = 'start_up.bat'
    start_up_location = 'C:\\Users\\' + username + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + start_up_bat
    try:
        with open(start_up_location, 'w') as start_up_file:
            with open(start_up_bat, 'r') as start_up:
                start_up_data = start_up.read()
                start_up_file.write(start_up_data)
    except IOError:
        print 'File not found.'

def install(username):
    start_up = 'startup.py'
    start_up_script = 'C:\\Users\\' + username
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

def install_StartUpNotifier():
    install('HP')
    get_startup_location('HP')

install_StartUpNotifier()
