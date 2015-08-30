# Playing with Eventbrite 
# From https://www.eventbrite.com/developer/v3/quickstart/ and 
# https://pypi.python.org/pypi/eventbrite/3.2.0
# https://github.com/eventbrite/eventbrite-sdk-python
# https://www.eventbrite.com/developer/v3/endpoints/users/ == formate of eb.get('users/me/...')
# Developer: Ginny C Ghezzo 
# Not sure the difference of ventbrite.get user2 = eb.get('/users/me')
# What I learned: 

import requests 
from eventbrite import Eventbrite
import sys 

if len(sys.argv) > 1:
	mykey = sys.argv[1]
else: 
	mykey = input('Shhh... what is your private key: ')
#response = requests.get()
eb = Eventbrite(mykey)
user = eb.get_user()				# why not use eventbrite.get user2 = eb.get('/users/me')
print('**User Information**')
for q in user:
	print(q, ' = ', user[q])
# I have no idea how to get the ids from the user 
print(eb.__dir__())
