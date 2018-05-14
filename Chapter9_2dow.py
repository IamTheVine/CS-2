# Python for Beginners Immersion Course
# Exercise 9.2
# Albert Molina
# 13-May-2018
# Description : Write a program that categorizes each mail message by which day of the week the commit was done. 
#           To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# Day of the week position. x column after split
LinePos = 3

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
		DayOfWeek = Words[LinePos-1]
	except :
		continue

	FileDict[DayOfWeek] = FileDict.get(DayOfWeek, 0) + 1

print(FileDict)
