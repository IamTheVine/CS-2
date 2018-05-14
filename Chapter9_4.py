# Python for Beginners Immersion Course
# Exercise 9.4
# Albert Molina
# 15-May-2018
# Description : After all the data has been read and the dictionary has been created, 
#      look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.


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
	except :
		continue

	FileDict[LineVal] = FileDict.get(LineVal, 0) + 1


# Get the email address with the most message
MostMsg = ''
MaxMsg = 0
for DictKey, DictVal in FileDict.items() :
	if DictVal > MaxMsg :
		MostMsg = DictKey
		MaxMsg = DictVal

	# In case there are email addresses that has the same max messages
	elif DictVal == MaxMsg :
		MostMsg = MostMsg + ', ' + DictKey

print(MostMsg + ' : ' + str(MaxMsg) )
