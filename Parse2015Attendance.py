# This script is created to process attendance from a TechGirlz Event 
# 	Get the .csv from EventBrite 
# 	
# 	For each line
#		Is this a new event? If yes then check if the person is already processed 
#		Get email (or Attendee name -- some key )
# 		Check if they are in there
#			If yes, then increment their shows or noshows 
#			IF no, add them 
#		Consider adding an input back in file = input("What is the file to parse ")

import csv
import datetime
import sys
if len(sys.argv) > 1:
	file = sys.argv[1]
else: 
	file = 'report1.csv'
	nextFile = 'lego1601.csv'
print(file, " ", nextFile)

try:
	f = open(file)
	nf = open(nextFile)
	eventCSV = csv.DictReader(f)
	nextEvent = csv.DictReader(nf)
except (IOError, ValueError): 
	print("An I/O Error or Value occurred. No file. We are DONE HERE!!! ")
	exit()		#Not sure if this is needed ... TODO think about this 

attendees = {}		# Dictinoary of sets 
oneShows = set()
shows = set()
twoNoShows = set()
allEvents = set()
allEmails = set()
count = 0 

for row in eventCSV: 
	count += 1
	email = row['Email']
	status = row['Attendee Status']
	eventName = row['Event Name']
	allEvents.add(eventName)
	allEmails.add(email)
	if  not (email in attendees):
		attendees[email] = [],[]
	if status == 'Checked In': 
		attendees[email][0].append(eventName)
	else: 	# Either Attending or Not Attending 
		attendees[email][1].append(eventName)
for i in attendees: 
	# print("Email ", i)
	# print("   Attended: ",len(attendees[i][0]))
	# print("   Missed: ",len(attendees[i][1]))
	if len(attendees[i][1]) >= 2: 
		twoNoShows.add(i)
	elif len(attendees[i][1]) == 1: 
		oneShows.add(i)
	else: 
		shows.add(i)

print("\n", "***","\n")
print("TechGirlz of the Triange Attendance Summary (2H2015*)")
print("    Total Records: ", count)
print("    Total Unique Emails", len(allEmails))
print("    Perfect Attendance " , len(shows))
print("    Missed one event " , len(oneShows))
print("    Missed two or More events " , len(twoNoShows))
print("Events with check-in: ", len(allEvents))
for i in allEvents: 
	print("   ",i)
print("WaitListers ")
for i in twoNoShows: 
	print("   ",i)

#Loop through the registration for the next event and see if there is an email match from twoNoShows
for row in nextEvent:
	email = row['Email']
	if email in twoNoShows:
		print(email, " Potentially missed two events")
		print("   Attended: (", len(attendees[email][0]),")") 
		for i in attendees[email][0]: print("    ", i)
		print("   Missed: (", len(attendees[email][1]),")") 
		for i in attendees[email][1]: print("    ", i)
		print(" ")
