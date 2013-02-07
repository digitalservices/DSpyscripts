# Basic log file parsing (Apache server used by Millennium)
# Each log entry stores the following:

# make regular expressions accessible to python
import re

# create a pattern (note the the 'r' before the quotes avoids the \ problem
patLocateFirstEntry = re.compile(r'^#\s{17}1$')
patLocateNextEntry = re.compile(r'^#\s{17}[0-9]+$')
patDatePlaced = re.compile(r'^Date Placed')
patDatePlacedDate = re.compile(r'[0-9]{2}-[0-9]{2}-[0-9]{4}')
	
# Ask for filename to open
#whichFileToRead = raw_input("File Name? ")
whichFileToRead = 'itemholds.txt'

# Open requested file
try:
	useTextFile = open(whichFileToRead, "r")
except IOError:
	print("file does not exist" + "\n")
	closeCommandWindow = raw_input("Press return to exit.")

# Open file to save to
#newFileName = whichFileToRead[0:whichFileToRead.rfind(".")] + "_output.txt"
#saveTextFile = open(newFileName, "w")	

# Set up variables
storeInfo = []
tempList = []

# Do stuff with file

line = useTextFile.readline()
while line:
	if patLocateFirstEntry.search(line): #find the first entry in the file
		line = useTextFile.readline()
		break
	line = useTextFile.readline()
while line:
	print(line)
	if patLocateNextEntry.search(line):
		print(line)
		storeInfo.append(tempList)
		tempList = []
	else:
		if patDatePlaced.search(line):
			print(patDatePlacedDate.findall(line))
			tempList.append(patDatePlacedDate.findall(line))
	line = useTextFile.readline()	
		

				
# close opened file when done
useTextFile.close()
#saveTextFile.close()

# hold command window open until user input detected
closeCommandWindow = raw_input("Press return to exit.")