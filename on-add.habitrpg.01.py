#!/usr/bin/env python

import sys
import json
import requests

URL = 'https://habitica.com/api/v2'
API_KEY = ''
API_USER = ''

headers = {
		'Content-Type' : 'application/json',
		'x-api-user' : API_USER,
		'x-api-key' : API_KEY
	}

def main():
	jsonTask = json.loads(sys.stdin.readline())
	
	id = pushTask(jsonTask)
	if not id == "":	
		jsonTask["id_habitica"] = id
	
	print(json.dumps(jsonTask))
	
	print "Task added on Habitica"

def pushTask( jsonTask ):
	values = {
		"type" : "todo",
		"text" : jsonTask["description"],
		"notes" : "Created from Taskwarrior"
		}
		
	req = requests.post(URL + '/user/tasks', data=json.dumps(values), headers=headers)
	
	jsonHabiticaTask = json.loads(req.text)
	value = '';
	try:
		vError = jsonHabiticaTask["err"]
		print "Error while pushing task to Habitica : " + vError 
	except:	
		try:
			value = jsonHabiticaTask["id"]
		except:
			value = ""
	
	return value
	
try:
	main()
except:
	print "Error! Unable to add task to Habitica"
sys.exit(0)
	
