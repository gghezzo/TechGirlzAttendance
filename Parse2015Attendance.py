# This script is created to process attendance from a TechGirlz Event 
# 	Get the .csv from EventBrite 
# 	
# 	For each line
#		Is this a new event? If yes then check if the person is already processed 
#		Get email (or Attendee name -- some key )
# 		Check if they are in there
#			If yes, then increment their shows or noshows 
#			IF no, add them 

import csv
import datetime

file = input("What is the file to parse ")
print(file)
try:
	f = open(file)
	eventCSV = csv.DictReader(f)
except (IOError, ValueError): 
	print("An I/O Error or Value occurred. No file. We are DONE HERE!!! ")
	exit()		#Not sure if this is needed ... TODO think about this 

attendees = {}
oneShows = set()
shows = set()
twoShows = set()
for row in eventCSV: 
	# print(row['Email'])
	# print(row['Attendee Status'])
	email = row['Email']
	status = row['Attendee Status']
	eventName = row['Event Name']
	if  not (email in attendees):
		attendees[email] = [],[]
	if status == 'Checked In': 
		attendees[email][0].append(eventName)
	else: 	# Either Attending or Not Attending 
		attendees[email][1].append(eventName)


# print(attendees)
for i in attendees: 
	print("Email ", i)
	print("   Attended: ",len(attendees[i][0]))
	print("   Missed: ",len(attendees[i][1]))
	if len(attendees[i][1]) >= 2: 
		twoShows.add(i)
	elif len(attendees[i][1]) == 1: 
		oneShows.add(i)
	else: 
		shows.add(i)
print("Two or More Noshows) " , len(twoShows))
print(twoShows)
print("One No Shows " , len(oneShows))
print("Shows " , len(shows))


