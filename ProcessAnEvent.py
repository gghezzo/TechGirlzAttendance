
# This script is created to process attendance from a TechGirlz Event 
# 	Get the .csv from EventBrite 
#	For those who did not show, update the master " No show" attendance list 
#		Consider creating a new master with the date - http://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
# 	For those who did show up, remove them from the "No Show " attendance list 
#   Create a summary for Diedre: Event Name, Total Attendes (with names), Total Unregistered (with names), Total No Shows (with names)

import datetime 
import csv

def outputReport():
	print("Triangle TechGirlz Summary")
	print("	Current Repeat No Shows: ")
	print("	Events Included: ")
	print("Event Name:")
	print("	No Shows Totals: ")
	print("	Not Attendee Total: ")
	print("	Attendee Total: ")


# Dear Main, I miss you! 
lastEvent = input("What is the event File: ")
#todo: wrap in error handling and check if a .csv 
#todo: Think about how toget the masterList = 
masterNoShowList = 'TechGirl_' + str(datetime.date.today()) + '.csv'

try:
	f = open(lastEvent)
	eventCSV = csv.DictReader(f)
except (IOError, ValueError): 
	print("An I/O Error or Value occurred. No file. We are DONE HERE!!! ")
	exit()
	# Should I set a file value 

eventDict = {}
eventName = None
for row in eventCSV:
	if eventName is None: event = row['Event Name']
	if row['Attendee Status'] == 'Attending':
		# processNoShows(row)
		key = row['Attendee #']
		# Need more columns todo 
		anotherdict[key] = (row['First Name']+ ' ' + row['Last Name'])
	elif row['Attendee Status'] == 'Not Attending':
		# processNotAttendee
		print("do something")
	elif row['Attendee Status'] == 'Checked In':
		# processAttendees
		print("do something")
	else: 
		print("There was a problem with ", str(row))
outputReport()
