import time
import requests
from pprint import pprint
api_url = 'https://api.rct2008.com:8443/{token}/{method}'
p_token = {Your own potato bot token}
my_chat_id = {Your own potato chat_id}


def send_potato_message(message):
    p_url = api_url.format(token=p_token, method='sendTextMessage')
    data = {
        'chat_type': 1, 
        'chat_id': my_chat_id,
        'text': message
    }
    r = requests.post(p_url, json=data)
    pprint(r.json())


def get_potato_message():
    p_url = api_url.format(token=p_token, method='getUpdates')
    p_json = requests.get(p_url).json()
    if p_json['result']:
        p_message = p_json['result'][0]['message']['text']
    else:
        p_message = None
    return p_message


if __name__ == '__main__':
    p_msg = None
    send_potato_message('nice to meet you :)')
    while 1:
        p_msg = get_potato_message()
        if p_msg is not None:
            send_potato_message(p_msg)
        time.sleep(1)
