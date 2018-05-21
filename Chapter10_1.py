# Python for Beginners Immersion Course
# Exercise 10.1
# Albert Molina
# 15-May-2018
# Description :  Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
#   Count the number of messages from each person using a dictionary.
#   After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
#   Then sort the list in reverse order and print out the person who has the most commits.


# Sender position in an email message. x column after split. This program is the same as Exercise 9.2, this LinePos variable is the only difference.
LinePos = 2

try :
	InpFile = input('Enter filename : ')
	FileHandler = open(InpFile)
except :
	print('Please input valid filename')
	exit()

FileDict = dict()

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

	# Search the key, if found add 1, if not found create a new key with value 1 as initial.
	FileDict[LineVal] = FileDict.get(LineVal, 0) + 1

# Using tupples and list, get the email address with the most message
NewTup = sorted( [(val, key) for key, val in FileDict.items() ], reverse=True ) 
HighVal, HighEmail = NewTup[0]
print(HighEmail, '  ' + str(HighVal))
