import time
import random
from potato_bot.potato_msg_demo import send_potato_message, get_potato_message
from potato_bot.combine_1 import parse_message, get_wea_json
from potato_bot.potato_demo_1 import basic_wea, spec_wea
responses = {
    'inform': [
        'I know {0}, let me check and wait a second...'
    ],
    'greet': [
        'hello, i am a weather bot, what can i do for you ?',
        'nice to meet you, i know the current weather all around the world, what do you want to know ?',
        'lucky you ! i am a current weather bot, ask me anything you want to know about the weather !'
    ],
    'goodbye': [
        'oh, i\'ll miss you, have a nice day !',
        'goodbye me friend, enjoy your day !',
        'bye, wish you have a great day XD'
    ],
    'thank': [
        'that\'s my pleasure XD',
        'you are very welcome :)',
        'Not at all ^_^'
    ],
    'default': [
        'Sorry, I can\'t understand :(, let us talk sth about weather !',
        'i am too fool to understand you QAQ , maybe say something about weather ?',
        'i am just a weather robot, how about talking something about weather ?'
    ]
}


def resp_wea_2(message, c_name, w_ele):
    intent, n_c_name, n_w_ele, intent_confidence = parse_message(message)
    if intent_confidence >= 0.55:
        if intent == 'inform':
            if n_c_name is not None and c_name != n_c_name:
                if c_name is not None:
                    w_ele = None
                c_name = n_c_name
            if n_w_ele is not None:
                w_ele = n_w_ele
            if c_name is not None:
                wea_json = get_wea_json(c_name)
                if n_c_name is not None:
                    send_potato_message(random.choice(responses['inform']).format(c_name))
                    basic_wea(wea_json)
                if w_ele is not None:
                    spec_wea(wea_json, w_ele)
            elif c_name is None:
                send_potato_message('tell me, which city\'s condition you want to know ?')
        elif intent == 'greet':
            send_potato_message(random.choice(responses['greet']))
        elif intent == 'thank':
            send_potato_message(random.choice(responses['thank']))
        elif intent == 'goodbye':
            send_potato_message(random.choice(responses['goodbye']))
    else:
        send_potato_message(random.choice(responses['default']))
    return c_name, w_ele


if __name__ == '__main__':
    send_potato_message('nice to meet you :)')
    c_name, w_ele = None, None
    while 1:
        p_msg = get_potato_message()
        if p_msg is not None:
            n_c_name, n_w_ele = resp_wea_2(p_msg, c_name, w_ele)
            c_name, w_ele = n_c_name, n_w_ele
        time.sleep(1)
