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

file = input("What is the file to parse")
print(file)
try:
	f = open(file)
	eventCSV = csv.DictReader(f)
except (IOError, ValueError): 
	print("An I/O Error or Value occurred. No file. We are DONE HERE!!! ")
	exit()