from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
import requests

trainer = Trainer(config.load('config_spacy.yml'))
training_data = load_data('data-wea-en.json')
interpreter = trainer.train(training_data)


def parse_message(message):
    parsed_json = interpreter.parse(message)
    intent = parsed_json['intent']['name']
    intent_confidence = parsed_json['intent']['confidence']
    entities = parsed_json['entities']
    c_name, w_ele = None, None
    for i in entities:
        if i['entity'] == 'location':
            c_name = i['value']
        elif i['entity'] == 'element':
            w_ele = i['value']

    return intent, c_name, w_ele, intent_confidence


def get_wea_json(c_name):
    ow_url = 'https://api.openweathermap.org/data/2.5/{weather_forecast}?q={city_name}&units=metric'
    api_key = '&appid={TOKEN}'
    wea_url = ow_url.format(weather_forecast='weather', city_name=c_name) + api_key
    wea_json = requests.get(wea_url).json()
    return wea_json


if __name__ == '__main__':
    block1 = parse_message("How about the humidity in London?")
    block2 = parse_message("What is the weather like today?")
    block6 = parse_message("My mistake. I am in Osaka.")
    block7 = parse_message("What about the wind speed?")
    block9 = parse_message("I am planning my holiday to Osaka. Is it raining right now?")
    block3 = parse_message("hey there")
    block4 = parse_message("bye")
    block5 = parse_message("thank you")
    block8 = parse_message("123456")
    print(block1)
    print(block2)
    print(block6)
    print(block7)
    print(block9)
    print(block3)
    print(block4)
    print(block5)
    print(block8)
