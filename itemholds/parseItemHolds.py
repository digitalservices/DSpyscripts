# Basic log file parsing (Apache server used by Millennium)
# Each log entry stores the following:

# make regular expressions accessible to python
import re

# create a pattern (note the the 'r' before the quotes avoids the \ problem
#patLocateFirstLine = re.compile(r'^#\s{17}[0-9]+$')

	
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

	
# Do stuff with file
	for fileLine in useTextFile:
		if patLocateFirstLine.search(fileLine):
			print(fileLine)
				
# close opened file when done
useTextFile.close()
#saveTextFile.close()

# hold command window open until user input detected
closeCommandWindow = raw_input("Press return to exit.")