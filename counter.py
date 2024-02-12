import requests
import time
import json

def retrieve_messages():
    global num
    headers = {
        "authorization" : "authorisation token you can see in inspect element"
    }
    r = requests.get('https://discord.com/api/v9/channels/<channel id of the channel you wish to send>/messages', headers=headers)


    jsonn = json.loads(r.text)
    for value in jsonn:
        num = int(value['content'])
        break

retrieve_messages()

for count in range (0,1000):
    if count % 5 == 0:
        retrieve_messages()
    num = num + 1
    url = "https://discord.com/api/v9/channels/<channel id of the channel you wish to send>/messages"

    payload = {
        "content" : str(num)
    }

    headers = {
        "Authorization" : "authorisation token you can see in inspect element"
    }

    res = requests.post(url, payload, headers=headers)
    time.sleep(0.2)
