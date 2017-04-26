
import requests
from templates.text import TextTemplate
import config
import time
import webbrowser

Print("Reminder Initiated")

alarm_HH = input("Enter the hour you want to have a break")
alarm_MM = input("Enter the minute you want to have a break")

print("I will remind at " + alarm_HH + ":" + alarm_MM)

while True:
    now = time.localtime()
    if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
        webbrowser.open("https://www.youtube.com/watch?v=izGwDsrQ1eQ")
        break

    else:
        print("no reminder")
    timeout = 60 - now.tm_sec
    if nonBlockingRawInput('', timeout) == 'stop':
        break

