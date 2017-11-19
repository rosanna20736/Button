import requests
import RPi.GPIO as GPIO
import time


myurl = 'https://maker.ifttt.com/trigger/button_pressed/with/key/pdleupkii6JTCj0vkLYJPGu8SFVJqDRyF3cvd6rNkg5'

blue_channel = 15
red_channel = 14
purple_channel = 4
black_channel = 18
channel_list = [blue_channel, red_channel, purple_channel, black_channel]


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
    # requests.get(myurl, params = {'value1' : val})


GPIO.setmode(GPIO.BCM)

for channel in range(0, len(channel_list)):
    print(channel_list[channel])
    GPIO.setup(channel_list[channel], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(channel_list[channel], GPIO.RISING, callback = my_callback)
#
# while True:
#     #time.sleep(0.2)
#
#     if GPIO.event_detected(blue_channel):
#         print ('blue pressed')
#         #requests.get(myurl, params = {'value1' : 'Big blue'})
#
#     if GPIO.event_detected(red_channel):
#         print ('red pressed')
#         #requests.get(myurl, params = {'value1' : 'Big red'})
#
#     if GPIO.event_detected(purple_channel):
#         print ('purple pressed')
#         #requests.get(myurl, params={'value1': 'Small purple'})
#
#     if GPIO.event_detected(black_channel):
#         print ('black pressed')
#         #requests.get(myurl, params = {'value1' : 'Small black'})



