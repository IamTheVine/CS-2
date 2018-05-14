# Python for Beginners Immersion Course
# Exercise 9.5
# Albert Molina
# 15-May-2018
# Description :  This program records the domain name (instead of the address) where the message was sent from instead 
#   of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# Sender position in an email message. x column after split. This program is the same as Exercise 9.2, this LinePos variable is the only difference.
LinePos = 2

try :
	InpFile = input('Enter filename : ')
except :
	print('Please input valid filename')
	exit()

FileDict = dict()
FileHandler = open(InpFile)

for line in FileHandler :
	LineFilter = line.upper()
	LineFilter = LineFilter.strip()

	if LineFilter[0:4] != 'FROM' :
		continue

	Words = line.split()
	try :
		LineVal = Words[LinePos-1]
		LineValsplit = LineVal.split('@')
		LineValCom = LineValsplit[1]
	except :
		continue

	FileDict[LineValCom] = FileDict.get(LineValCom, 0) + 1

print(FileDict)
