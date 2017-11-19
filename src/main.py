import requests
import RPi.GPIO as GPIO
import time


myurl = 'https://maker.ifttt.com/trigger/button_pressed/with/key/pdleupkii6JTCj0vkLYJPGu8SFVJqDRyF3cvd6rNkg5'

blue_channel = 15
red_channel = 14
purple_channel = 4
black_channel = 26
channel_list = [blue_channel, red_channel, purple_channel, black_channel]

GPIO.setmode(GPIO.BCM)

def my_callback(channel):
    if channel == blue_channel:
        val = "Big blue"
    elif channel == red_channel:
        val = "Big red"
    elif channel == purple_channel:
        val = "Small purple"
    elif channel == black_channel:
        val = "Small black"
    else:
        val = "unknown"
    print('Edge detected on channel %s' % val)
    requests.get(myurl, params = {'value1' : val})

for channel in channel_list:
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(channel, GPIO.RISING, callback = my_callback, bouncetime = 1000)

print('ready')

while True:
    pass




