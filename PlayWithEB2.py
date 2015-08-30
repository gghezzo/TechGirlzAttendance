# Playing with Eventbrite, with Focus 
# Developer: Ginny C Ghezzo 
# What can I do https://www.eventbrite.com/developer/v3/endpoints/

import requests 
from eventbrite import Eventbrite
import sys 
import os
# Globals - I think 
Deirdre = '7544636337'
RoundTable = '17411466164'
keysToUse = open('keyoptions.txt','w')
recordKeys = False

# Get the personal oauth key TODO: Think about doing this better  (check length, etc)
#Let the magic happen here! 
def main(): 
	print('Go main, beat ... no idea what the analogy is')
	print(mykey)				# why is this a global
	# Get connected 	# Display who I am 
	eb = setup_connection()
	# Display my events 
	list_myevents(eb)
	# Find an event that is not mine 
	list_anyevents(eb)
	# Find Deidre's events or TechGirlz 
	tellmeAbout(eb,Deirdre)
	# List who attended, who did not, 
	findEventsBy(eb, Deirdre)

def setup_connection():
	eb = Eventbrite(mykey)
	#if recordKeys == True: keysToUse.write(str('eb = ',str(eb) ))
	user = eb.get_user()
	#if recordKeys == True: keysToUse.write(str('user = ',user.keys()) )
	# check if we connected 
	try:
		print('Here is the user id ', user['id'])
		return eb
	except KeyError:
		print('This will not go well')
		exit()
def list_myevents(eb):
	print('*** My Events ***')
	myevents = eb.get('/users/me/owned_events')
	e = myevents['events'][0]['name']['text']
	#if recordKeys == True: keysToUse.write('Events = ',myevents.keys() )
	#if recordKeys == True: keysToUse.write('An Events = ',myevents['events'][0].keys() )
	print('   Name of my event',e)
def list_anyevents(eb, id='17411466164'):				# fix this so it is a function and pass in 
	print('*** Any Events ***')
	e = eb.get('/events/'+id)
	print(list(e.keys()))
	print('   ',e['name']['text'])
def tellmeAbout(eb, id):
	print('*** Tell me about An Organizer ***')
	e = eb.get('/organizers/'+id)
	for x in e: 										# BAD variables. Don't tell the professor! 
		print('   ',x,' = ',e[x])
def findEventsBy(eb, id):
	print('*** List of public Events Organized by ***')
	e = eb.event_search(**{'organizer.id':id})
	for x in e['events']: 
		print('   = ',x['name']['text'])

if __name__== "__main__": 
	if not sys.argv[1:]:
		mykey = input('Shhh... what is your private key: ')
	else:
		mykey = sys.argv[1]
	recordKeys = True
	main()
	keysToUse.close()
	print('We are leaving now')