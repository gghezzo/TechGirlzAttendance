# Playing with Eventbrite, with Focus 
# Developer: Ginny C Ghezzo 
# Not sure the difference of ventbrite.get user2 = eb.get('/users/me')

import requests 
from eventbrite import Eventbrite
import sys 
import os
# Globals - I think 


# Get the personal oauth key TODO: Think about doing this better  (check length, etc)
'''
if len(sys.argv) > 1:
	mykey = sys.argv[1]
else: 
	mykey = input('Shhh... what is your private key: ')
	'''

#Let the magic happen here! 
def main(): 
	print('Go main, beat ... no idea what the analogy is')
	print(mykey)				# why is this a global
	# Get connected 	# Display who I am 
	eb = setup_connection()
	# Display my events 
	list_myevents(eb)
	# Find an event that is not mine 
	# Find Deidre's events or TechGirlz 
	# List who attended, who did not, 

def setup_connection():
	eb = Eventbrite(mykey)
	user = eb.get_user()
	# check if we connected 
	try:
		print('Here is the user id ', user['id'])
		return eb
	except KeyError:
		print('This will not go well')
		exit()
def list_myevents(eb):
	myevents = eb.get('/users/me/owned_events')
	print(myevents)


print(__name__)
if __name__== "__main__": 
	if not sys.argv[1:]:
		mykey = input('Shhh... what is your private key: ')
	else:
		mykey = sys.argv[1]
	main()
	print('We are leaving now')