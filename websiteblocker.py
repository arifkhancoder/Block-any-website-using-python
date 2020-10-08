
import time
from _datetime import datetime

path = "C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'

block_list = ['facebook.com', 'www.facebook.com', 'gmail.com', 'www.gmail.com']

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9) < datetime(datetime.now().year,
                                                                                             datetime.now().month,
                                                                                             datetime.now().day, 18):
        with open(path, 'r+') as file:
            content = file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirec + ' ' + website + '\n')
        print('All listed websites are blocked')
        break
    else:

        with open(path, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()
        print('websites are unblocked :-) ')
        break
        
