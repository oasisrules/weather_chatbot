import time
from potato_bot.combine_1 import parse_message
from potato_bot.combine_2 import get_wea_json
from potato_bot.potato_msg_demo import send_potato_message
from potato_bot.potato_msg_demo import get_potato_message


def basic_wea(wea_json):
    num = 0
    wea_main = ''
    description = ''
    for wea in wea_json['weather']:
        wea_main += wea['main']
    for wea in wea_json['weather']:
        if num > 0:
            description += 'and '
        description += wea['description'] + ' '
        num += 1
    if wea_main == 'Clouds' or num > 1:
        send_potato_message('There are ' + description + 'in ' + wea_json['name']
                            + ' right now. The outdoor temperature is ' + str(wea_json['main']['temp']) + '℃.')
    else:
        send_potato_message('There is ' + description + 'in ' + wea_json['name']
                            + ' right now. The outdoor temperature is ' + str(wea_json['main']['temp']) + '℃.')


def spec_wea(wea_json, w_ele):
    description = ''
    for wea in wea_json['weather']:
        description += wea['description'] + ' '
    ele_set = ['temp', 'pressure', 'humidity', 'wind speed', 'rain', 'snow']
    if w_ele in ele_set:
        if w_ele == 'temp':
            pass
        elif w_ele == 'pressure':
            send_potato_message('The pressure is ' + str(wea_json['main']['pressure']) + 'hPa')
        elif w_ele == 'humidity':
            send_potato_message('The humidity is ' + str(wea_json['main']['humidity']) + '%')
        elif w_ele == 'wind speed':
            send_potato_message('The wind speed is ' + str(wea_json['wind']['speed']) + 'm/s')
        elif w_ele == 'rain':
            if 'rain' in description:
                send_potato_message('It is raining right now. I recommend you to take an umbrella.')
            else:
                send_potato_message('Don\'t worry, it is not raining right now.')
        elif w_ele == 'snow':
            if 'rain' in description:
                send_potato_message('It is snowing right now. Try to wear some warm clothes.')
            else:
                send_potato_message('Don\'t worry, it is not snowing right now.')
    else:
        send_potato_message('sorry, i can\'t find the information you want :(')


if __name__ == '__main__':
    send_potato_message('nice to meet you :)')
    while 1:
        p_msg = get_potato_message()
        if p_msg is not None:
            resp_wea_1(p_msg)
        time.sleep(1)

# I am planning my holiday to Osaka. I wonder what is the weather out there.
# How about the humidity in London?
# What is the temperature in Tokyo right now?
# How about the wind speed in London?
# I am planning my holiday to Osaka. Is it raining right now?
