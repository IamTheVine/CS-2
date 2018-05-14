# Python for Beginners Immersion Course
# Exercise 9.3
# Albert Molina
# 13-May-2018
# Description : Write a program to read through a mail log, build a histogram using a dictionary 
#     to count how many messages have come from each email address, and print the dictionary.


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

print(FileDict)
