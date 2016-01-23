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
if len(sys.argv) > 2:
	file = sys.argv[1]
	nextFile = sys.argv[2]
else: 
	file = 'report1.csv'
	nextFile = 'lego1601.csv'
try:
	f = open(file)
	nf = open(nextFile)
	eventCSV = csv.DictReader(f)
	nextEvent = csv.DictReader(nf)
except (IOError, ValueError): 
	print("An I/O Error or Value occurred. No file. We are DONE HERE!!! ")
	exit()	

# Need to think about if we need all these 
attendees = {}			# Dictinoary of sets 
oneNoShows = set()
shows = set()
twoNoShows = set()
allEvents = set()
allEmails = set()
unRegistered = set()
count = 0 
date = datetime.datetime.today().strftime('%m/%d/%Y')

# Loop through every record in the file 
# How do we check if one email is used for multiple attendees. 
for row in eventCSV: 
	count += 1
	email = row['Email']
	status = row['Attendee Status']
	eventName = row['Event Name']
	allEvents.add(eventName)
	allEmails.add(email)
	if  not (email in attendees):
		attendees[email] = set(),set(),set()
	if status == 'Checked In': 
		attendees[email][0].add(eventName)
	elif status == 'Not Attending': 	# Attending  
		attendees[email][1].add(eventName)
	else: 	# Did not show 
		attendees[email][2].add(eventName)

for i in attendees: 
	if len(attendees[i][2]) >= 2: 
		twoNoShows.add(i)
	elif len(attendees[i][2]) == 1: 
		oneNoShows.add(i)
	else: 
		shows.add(i)
	# If they unregistered we want to give them credit 
	if len(attendees[i][1]) > 0: 
		unRegistered.add(i)


print("\n", "*** Report Date: ",date,"***")
print("TechGirlz of the Triange Attendance Summary (2H2015*)")
print("    Total Records: ", count)
print("    Total Unique Emails", len(allEmails))
print("    Perfect Attendance " , len(shows))
print("    Missed one event " , len(oneNoShows))
print("    Missed two or More events " , len(twoNoShows))
print("    Unregistered", len(unRegistered))
print("\n","Events with check-in: ", len(allEvents))
for i in allEvents: 
	print("   ",i)
print("\n","WaitListers (Two or More No shows) ", len(twoNoShows))
for id in twoNoShows: 
	print("  ID:",id)
	print("     Attended: (", len(attendees[id][0]),")") 
	for a in attendees[id][0]: print("      ", a)
	print("     Unregistered : (", len(attendees[id][1]),")") 
	for a in attendees[id][1]: print("      ", a)
	print("     Missed: (", len(attendees[id][2]),")") 
	for a in attendees[id][2]: print("      ", a)

print("\n","Unregistered (Not Attending) ", len(unRegistered))
for i in unRegistered: 
	print("   ",i)

#Loop through the registration for the next event and see if there is an email match from twoNoShows
print("\n","Potential People to Waitlist for ",nextFile)
for row in nextEvent:
	email = row['Email']
	if email in twoNoShows:
		print("  ID: ",email)
		print("     Attended: (", len(attendees[email][0]),")") 
		for i in attendees[email][0]: print("      ", i)
		print("     Unregistered : (", len(attendees[email][1]),")") 
		for i in attendees[email][1]: print("      ", i)
		print("     Missed: (", len(attendees[email][2]),")") 
		for i in attendees[email][2]: print("      ", i)
		print(" ")
