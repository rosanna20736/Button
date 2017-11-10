import requests


myurl = 'https://maker.ifttt.com/trigger/button_pressed/with/key/pdleupkii6JTCj0vkLYJPGu8SFVJqDRyF3cvd6rNkg5'

requests.get(myurl, params = {'value1' : 'Blue'})


