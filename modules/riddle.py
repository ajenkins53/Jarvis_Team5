import requests
from templates.text import TextTemplate
from random import choice
import json
import config

def process(input, entities = None):
	output = {}
	try:
		'''
		# Programming riddles
		r = requests.get('http://quotes.stromconsultancy.co.uk/random.json') 
		data = r.json()
		output['input'] = input
		output['output'] = TextTemplate(data['quote'] + ' _ ' + data['author']).get_message()
		output['success'] = True
		'''
		with open(config.RIDDLES_SOURCE_FILE) as riddles_file:
			riddles = json.load(riddles_file)
			riddles_list = riddles['riddles']
			output['input'] = input
			output['output'] = TextTemplate(choice(riddles_list)).get_message()
			output['success'] = True
	except:
		output['success'] = False
	return output
