import requests
import RPi.GPIO as GPIO
import time

myurl = 'https://maker.ifttt.com/trigger/button_pressed/with/key/pdleupkii6JTCj0vkLYJPGu8SFVJqDRyF3cvd6rNkg5'

blue_channel = 15
red_channel = 14
purple_channel = 4
black_channel = 18
channel_list = [blue_channel, red_channel, purple_channel, black_channel]

GPIO.setmode(GPIO.BCM)

for channel in range(0, len(channel_list)):
    print(channel_list[channel])
    GPIO.setup(channel_list[channel], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(channel_list[channel], GPIO.RISING)

while True:
    time.sleep(0.2)

    if GPIO.event_detected(blue_channel):
        requests.get(myurl, params = {'value1' : 'Big blue'})

    elif GPIO.event_detected(red_channel):
        requests.get(myurl, params = {'value1' : 'Big red'})

    elif GPIO.event_detected(purple_channel):
        requests.get(myurl, params={'value1': 'Small purple'})

    elif GPIO.event_detected(black_channel):
        requests.get(myurl, params = {'value1' : 'Small black'})