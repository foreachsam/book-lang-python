#!/usr/bin/env python3

## http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

import requests

req = requests.get('https://api.github.com/')

#print(req)
## <Response [200]>

#print(type(req))
## <class 'requests.models.Response'>


## https://developer.github.com/v3/
