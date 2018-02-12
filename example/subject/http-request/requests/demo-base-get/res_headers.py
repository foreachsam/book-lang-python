#!/usr/bin/env python3

## http://docs.python-requests.org/en/master/user/quickstart/#response-content

import requests

res = requests.get('https://api.github.com/')

#print(res.headers)

#print(type(res.headers))
## <class 'requests.structures.CaseInsensitiveDict'>


for key in res.headers:
	val = res.headers[key]
	## https://docs.python.org/3/library/stdtypes.html#dict.get
	#val = res.headers.get(key)
	#val = res.headers.get(key, '')

	#print(key)
	#print(val)

	## https://docs.python.org/3/library/string.html#formatstrings
	## https://docs.python.org/3/library/string.html#formatexamples
	#line = '{key}: {val}'.format(key=key, val=val)
	line = '{}: {}'.format(key, val)
	print(line)


## https://developer.github.com/v3/
