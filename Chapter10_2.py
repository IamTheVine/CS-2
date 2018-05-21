# Python for Beginners Immersion Course
# Exercise 10.2
# Albert Molina
# 20-May-2018
# Description :  This program counts the distribution of the hour of the day for each of the messages. 
#   You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. 
#   Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.


# Hour of the day position in an email message. x column after split. 
LinePos = 6

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
		LineSplit2 = Words[LinePos-1]
		LineSplit2 = LineSplit2.split(':')
		LineVal = LineSplit2[0]
	except :
		continue

	# Search the key, if found add 1, if not found create a new key with value 1 as initial.
	FileDict[LineVal] = FileDict.get(LineVal, 0) + 1


# Using tupples and list, print the 
NewLstTup= sorted( [(key, val) for key, val in FileDict.items()]) 
for key, val in NewLstTup :
	print(key + '  ' + str(val))
