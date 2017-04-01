import requests
from templates.text import TextTemplate
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://pebble-pickup.herokuapp.com/tweets/random') 
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['tweet']).get_message()
        output['success'] = True
        '''
        with open(config.PICKUP_SOURCE_FILE) as pickup_file:
            pick up lines = json.load(pickuplines_file)
            pickup_list = pickup['pick up lines']
            output['input'] = input
            output['output'] = TextTemplate(choice(pickup_list)).get_message()
            output['success'] = True
    except:
        output['success'] = False
    return output
