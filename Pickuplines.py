import requests
from templates.text import TextTemplate
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://tambal.azurewebsites.net/joke/random') <-- change this link
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['pick up line']).get_message()
        output['success'] = True
        '''
        with open(config.PICKUP_SOURCE_FILE) as pickup_file:
            pick up lines = json.load(jokes_file)
            pickup_list = pickup['pick up lines']
            output['input'] = input
            output['output'] = TextTemplate(choice(pickup_list)).get_message()
            output['success'] = True
    except:
        output['success'] = False
    return output
