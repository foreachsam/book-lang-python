#!/usr/bin/env python3

## http://docs.python-requests.org/en/master/user/quickstart/#response-content

import requests

res = requests.get('https://api.github.com/')

print(res.text)

#print(type(res.text))
## <class 'str'>


## https://developer.github.com/v3/
