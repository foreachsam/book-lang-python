#!/usr/bin/env python3

## http://docs.python-requests.org/en/master/user/quickstart/#response-content

import requests

## https://developer.github.com/v3/repos/#list-user-repositories
res = requests.get('https://api.github.com/users/github/repos')

json = res.json()

for item in json:
	#print(item)

	#print(type(item))
	#<class 'dict'>

	#clone_url = item['clone_url']

	## https://docs.python.org/3/library/stdtypes.html#dict.get
	clone_url = item.get('clone_url', '')

	#print(clone_url)

	print('git clone {}'.format(clone_url))
